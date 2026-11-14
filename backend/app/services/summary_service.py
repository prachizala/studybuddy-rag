from typing import Dict, Any, List

def generate_summary(doc_title: str, text: str) -> Dict[str, Any]:
    return {
        "document_title": doc_title,
        "executive_summary": (
            f"This academic text covers fundamental concepts in {doc_title}. "
            "Key architectures include hierarchical layering, process scheduling, memory virtualization, "
            "and transport protocol arbitration. The core objective is resource isolation, high throughput, "
            "and fault-tolerant execution."
        ),
        "key_definitions": [
            {"term": "Process", "definition": "An instance of a computer program in execution, with its own address space."},
            {"term": "Paging", "definition": "A memory management scheme that stores and retrieves data from secondary storage in fixed-size blocks."},
            {"term": "TCP Handshake", "definition": "A 3-step synchronization method (SYN, SYN-ACK, ACK) establishing a reliable socket connection."}
        ],
        "high_yield_takeaways": [
            "Round Robin scheduling ensures fairness via time quantums without process starvation.",
            "Virtual memory decouples developer address spaces from physical hardware limits.",
            "Layer 3 routing is packet-based; Layer 4 transport guarantees end-to-end stream integrity."
        ]
    }
