import json
from pathlib import Path

from src.rag_assistant.pipeline import RAGPipeline


DATASET_PATH = Path("evaluation/eval_dataset.json")


def load_evaluation_dataset():
    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def evaluate():
    dataset = load_evaluation_dataset()
    pipeline = RAGPipeline(load_existing=True)

    total_questions = len(dataset)
    passed_questions = 0

    for index, item in enumerate(dataset, start=1):
        question = item["question"]
        expected_keywords = item["expected_keywords"]

        result = pipeline.query(question)
        answer = result["answer"]

        matched_keywords = [
            keyword
            for keyword in expected_keywords
            if keyword.lower() in answer.lower()
        ]

        passed = len(matched_keywords) > 0

        if passed:
            passed_questions += 1

        print(f"\nQuestion {index}: {question}")
        print(f"Answer: {answer}")
        print(f"Expected keywords: {expected_keywords}")
        print(f"Matched keywords: {matched_keywords}")
        print(f"Result: {'PASS' if passed else 'FAIL'}")

    accuracy = (
        passed_questions / total_questions * 100
        if total_questions
        else 0
    )

    print("\n" + "=" * 50)
    print(f"Questions evaluated: {total_questions}")
    print(f"Questions passed: {passed_questions}")
    print(f"Keyword Match Rate: {accuracy:.2f}%")
    print("=" * 50)


if __name__ == "__main__":
    evaluate()