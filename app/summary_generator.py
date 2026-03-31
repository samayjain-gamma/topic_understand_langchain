from app.config import get_llm
from app.prompts import summary_prompt
from app.utils.exception import CustomException
from app.utils.logger import logger
from app.utils.streaming import StreamHandler

stream_handler = StreamHandler()
llm = get_llm(stream=True, callbacks=[stream_handler])


def generate_summary(topic: str, subquestions: list[str], answers: list[str]) -> str:

    try:
        logger.info("Entered in to try block of summary generator")
        sub_q_a_text = ""
        for i, (q, a) in enumerate(zip(subquestions, answers), 1):
            sub_q_a_text += f"{i}. {q}\nAnswer: {a}\n\n"

        prompt = summary_prompt.format(
            topic=topic, subquestions_and_answers=sub_q_a_text.strip()
        )

        response = llm.invoke(prompt)
        summary = response.content.strip()

        logger.info("Summary generated successfully.")
        return summary

    except Exception as e:
        logger.error(print("failed to generate summary report"))
        raise CustomException(e)


if __name__ == "__main__":
    topic = "climate change impact on agriculture"
    subquestions = [
        "How do rising temperatures and extreme weather events affect crop productivity?",
        "What economic consequences does climate change impose on agricultural supply chains?",
        "What adaptation strategies are being implemented to protect food security?",
    ]
    answers = [
        "Rising temperatures reduce crop yields due to heat stress, floods, and droughts. Farmers must adapt through irrigation and resilient crop varieties.",
        "Economic consequences include disrupted supply chains, increased costs, and risk to farmer incomes. Markets may face price volatility and food insecurity.",
        "Adaptation strategies include drought-resistant crops, improved irrigation, early warning systems, and policy support for vulnerable communities.",
    ]

    report = generate_summary(topic, subquestions, answers)
    print(report)
