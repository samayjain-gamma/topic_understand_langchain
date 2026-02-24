from app.subquestion import generate_subquestions
from app.answer import generate_answer
from app.evaluator import evaluate_answer
from app.summary_generator import generate_summary
from app.utils.exception import CustomException
from app.utils.logger import logger

MAX_RETRIES = 2


def main():
    try:
        topic = input(f"Enter the topic name : ")
        if not topic:
            print("Topic cannot be empty")
            return
    
        subquestions = generate_subquestions(topic=topic)
        print(f"Generated subquestions -> \n")
        for i , ques in enumerate(subquestions, 1):
            print(f"{i}. {ques}")
        print(f"\n")


        answers = []

        for i , question in enumerate(subquestions, 1):
            print(f"\n Answering question {i} : {question}")
            retries = 0

            while retries < MAX_RETRIES:
                try:
                    answer = generate_answer(question=question)
                    verdict = evaluate_answer(question=question, answer=answer)

                    if verdict == "PASS":
                        print(answer)
                        answers.append(answer)
                        break
                    else:
                        retries += 1
                        print(f"\n[Retry {retries}/{MAX_RETRIES}] Answer did not pass evaluation.\n")
                        logger.warning(f"Retrying question: {question} ({retries}/{MAX_RETRIES})")

                except Exception as e:
                    retries += 1
                    print(f"\n[Retry {retries}/{MAX_RETRIES}] Error: {e}\n")
                    logger.error(f"Error during answer generation for question '{question}': {e}")

            if retries > MAX_RETRIES:
                print(f"\n[Skipped] Could not generate a satisfactory answer for question: {question}\n")
                answers.append("Answer could not be generated satisfactorily.")
    


        print("\nGenerating final summary...\n")
        report = generate_summary(topic, subquestions, answers)
        print("\n===== FINAL REPORT =====\n")
        print(report)



    except Exception as e:
        logger.error(f"Fatal error in the pipeline")
        raise CustomException(e)


if __name__ == "__main__":
    main()
    
