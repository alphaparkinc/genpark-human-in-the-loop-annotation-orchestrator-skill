class HumanInTheLoopAnnotationOrchestratorClient:
    def process_annotation(self, raw_dataset_item: dict, ai_confidence_threshold: float = 0.85) -> dict:
        score = raw_dataset_item.get("ai_confidence", 0.75)
        if score >= ai_confidence_threshold:
            status = "AUTO_ACCEPTED"
            reviewer = "SYSTEM_AGENT"
        else:
            status = "ROUTED_TO_HUMAN_REVIEW"
            reviewer = "HUMAN_QA_QUEUE"
        return {
            "annotation_status": status,
            "assigned_reviewer": reviewer
        }
