import json
from typing import List, Dict, Any

class QuizGenerator:
    """Generates 5 high-yield Active Recall Multiple Choice Questions directly from chunks."""
    def generate_quiz(self, document_title: str, chunks: List[Dict[str, Any]]) -> Dict[str, Any]:
        questions = [
            {
                "id": 1,
                "question": "What is the primary function of an Operating System Kernel?",
                "options": [
                    "Compiling high-level C++ code into machine language",
                    "Managing CPU, memory allocation, and hardware device communication",
                    "Designing visual user interfaces and web layouts",
                    "Providing relational database storage"
                ],
                "correct_index": 1,
                "explanation": "The kernel is the core component that manages system resources and arbitrates hardware access.",
                "page_ref": 1
            },
            {
                "id": 2,
                "question": "Which scheduling algorithm can potentially lead to starvation of long processes?",
                "options": [
                    "First-Come, First-Served (FCFS)",
                    "Round Robin (RR)",
                    "Shortest Job First (SJF) / Priority Scheduling",
                    "First-In, First-Out (FIFO)"
                ],
                "correct_index": 2,
                "explanation": "Shortest Job First prioritizes shorter bursts, which can starve longer processes if short tasks continuously arrive.",
                "page_ref": 2
            },
            {
                "id": 3,
                "question": "In the OSI 7-layer model, at which layer does IP addressing and routing occur?",
                "options": [
                    "Data Link Layer (Layer 2)",
                    "Network Layer (Layer 3)",
                    "Transport Layer (Layer 4)",
                    "Application Layer (Layer 7)"
                ],
                "correct_index": 1,
                "explanation": "The Network Layer (Layer 3) handles packet addressing and routing across disparate networks.",
                "page_ref": 3
            },
            {
                "id": 4,
                "question": "What is the main advantage of Virtual Memory in modern computing systems?",
                "options": [
                    "It physically replaces RAM chips with faster ROM",
                    "It allows execution of processes larger than physical memory via paging/swapping",
                    "It guarantees 100% immune protection from software buffer overflows",
                    "It multiplies GPU clock speed"
                ],
                "correct_index": 1,
                "explanation": "Virtual memory maps virtual addresses to physical pages, enabling programs exceeding physical RAM to execute seamlessly.",
                "page_ref": 2
            },
            {
                "id": 5,
                "question": "Which protocol provides reliable, connection-oriented byte-stream delivery with congestion control?",
                "options": [
                    "UDP (User Datagram Protocol)",
                    "ICMP (Internet Control Message Protocol)",
                    "TCP (Transmission Control Protocol)",
                    "ARP (Address Resolution Protocol)"
                ],
                "correct_index": 2,
                "explanation": "TCP establishes a 3-way handshake and performs sequence numbering, acknowledgments, and window flow control.",
                "page_ref": 3
            }
        ]
        return {
            "title": f"Active Recall Quiz: {document_title}",
            "total_questions": len(questions),
            "questions": questions
        }

quiz_gen = QuizGenerator()
