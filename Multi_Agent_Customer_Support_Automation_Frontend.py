import os

import streamlit as st
from crewai import Agent, Task, Crew
from crewai_tools import ScrapeWebsiteTool
from dotenv import load_dotenv

# Load variables from .env when present
load_dotenv()

os.environ.setdefault("OPENAI_MODEL_NAME", "gpt-4o-mini")

# Define agents
support_agent = Agent(
    role="Senior Support Representative",
    goal="Be the most friendly and helpful support representative in your team",
    backstory=(
        "You work at GenWizz (https://genwizz.com) and are now working on providing "
        "support to {customer}, a super important customer for your company. "
        "You need to make sure that you provide the best support! "
        "Make sure to provide full complete answers, and make no assumptions."
    ),
    allow_delegation=False,
    verbose=True
)

support_quality_assurance_agent = Agent(
    role="Support Quality Assurance Specialist",
    goal="Get recognition for providing the best support quality assurance in your team",
    backstory=(
        "You work at GenWizz (https://genwizz.com) and are now working with your team "
        "on a request from {customer} ensuring that the support representative is "
        "providing the best support possible.\n"
        "You need to make sure that the support representative is providing full"
        "complete answers, and make no assumptions."
    ),
    verbose=True
)

# Define tools
docs_scrape_tool = ScrapeWebsiteTool(
    website_url="https://genwizz.com/mobile-app-development"
)

# Define tasks
inquiry_resolution = Task(
    description=(
        "{customer} just reached out with a super important ask:\n"
        "{inquiry}\n\n"
        "{person} from {customer} is the one that reached out. "
        "Make sure to use everything you know to provide the best support possible."
        "You must strive to provide a complete and accurate response to the customer's inquiry."
    ),
    expected_output=(
        "A detailed, informative response to the customer's inquiry that addresses "
        "all aspects of their question.\n"
        "The response should include references to everything you used to find the answer, "
        "including external data or solutions. Ensure the answer is complete, "
        "leaving no questions unanswered, and maintain a helpful and friendly tone throughout."
    ),
    tools=[docs_scrape_tool],
    agent=support_agent,
)

quality_assurance_review = Task(
    description=(
        "Review the response drafted by the Senior Support Representative for {customer}'s inquiry. "
        "Ensure that the answer is comprehensive, accurate, and adheres to the "
        "high-quality standards expected for customer support.\n"
        "Verify that all parts of the customer's inquiry have been addressed "
        "thoroughly, with a helpful and friendly tone.\n"
        "Check for references and sources used to find the information, "
        "ensuring the response is well-supported and leaves no questions unanswered."
    ),
    expected_output=(
        "A final, detailed, and informative response ready to be sent to the customer.\n"
        "This response should fully address the customer's inquiry, incorporating all "
        "relevant feedback and improvements.\n"
        "Don't be too formal, we are a chill and cool company "
        "but maintain a professional and friendly tone throughout."
    ),
    agent=support_quality_assurance_agent,
)

crew = Crew(
    agents=[support_agent, support_quality_assurance_agent],
    tasks=[inquiry_resolution, quality_assurance_review],
    verbose=2,
    memory=True
)

def main():
    st.set_page_config(page_title="Customer Support", layout="centered")
    st.title("Customer Support 📞")

    if not os.getenv("OPENAI_API_KEY"):
        st.error("OPENAI_API_KEY is not set. Add it to your environment or .env file before running the app.")
        st.stop()

    if "history" not in st.session_state:
        st.session_state["history"] = []
    if "customer" not in st.session_state:
        st.session_state["customer"] = ""
    if "person" not in st.session_state:
        st.session_state["person"] = ""

    st.subheader("Chat with Customer Support Team")

    # Static input fields for customer and person
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            customer = st.text_input(
                "Customer Name",
                value=st.session_state["customer"],
                key="customer_static",
                placeholder="e.g. GenWizz"
            )
        with col2:
            person = st.text_input(
                "Person Name",
                value=st.session_state["person"],
                key="person_static",
                placeholder="e.g. Fahamgeer"
            )
        st.session_state["customer"] = customer
        st.session_state["person"] = person

    # Chat history display
    chat_placeholder = st.container()
    with chat_placeholder:
        for idx, entry in enumerate(st.session_state["history"]):
            st.markdown(f"**You:** {entry['inquiry']}")
            st.markdown(f"**Support:** {entry['response']}")
            st.markdown("---")

    # Static input field for new inquiry at the bottom
    st.markdown("### Type your message below:")
    # Use a local variable for inquiry, do not try to clear st.session_state["inquiry_static"]
    inquiry = st.text_area(
        "Your Message",
        key="inquiry_static",
        placeholder="Type your question here, e.g. 'I'm looking for a way to build a custom mobile application for my Clothing Store. I want to know if you have any solutions that can help me with this.'"
    )
    send = st.button("Send")

    if send and inquiry.strip():
        st.info("Processing... This may take a minute.")
        inputs = {
            "customer": st.session_state["customer"],
            "person": st.session_state["person"],
            "inquiry": inquiry
        }
        try:
            result = crew.kickoff(inputs=inputs)
            if isinstance(result, str):
                st.session_state["history"].append(
                    {"customer": st.session_state["customer"], "person": st.session_state["person"], "inquiry": inquiry, "response": result}
                )
            else:
                st.session_state["history"].append(
                    {"customer": st.session_state["customer"], "person": st.session_state["person"], "inquiry": inquiry, "response": str(result)}
                )
            # Do not attempt to clear st.session_state["inquiry_static"], just rerun to reset the text area
            st.rerun()
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
