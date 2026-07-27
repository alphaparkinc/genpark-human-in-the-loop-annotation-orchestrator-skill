from client import HumanInTheLoopAnnotationOrchestratorClient

def main():
    client = HumanInTheLoopAnnotationOrchestratorClient()
    res = client.process_annotation({"item_id": "IMG-901", "ai_confidence": 0.72}, 0.85)
    print(f"Status: {res['annotation_status']}")
    print(f"Reviewer: {res['assigned_reviewer']}")

if __name__ == "__main__":
    main()
