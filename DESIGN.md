# Design Specification
## StudyBuddy RAG: UI/UX & Component System

### 1. Visual Language & Aesthetics
StudyBuddy RAG is engineered around a distraction-free, high-focus dark slate and deep violet developer-style workstation.

- **Color Palette**:
  - **Void Canvas**: `#0b0f17` (Deep background canvas)
  - **Surface Container**: `#161e2e` (Card containers, panel borders)
  - **Electric Indigo**: `#6366f1` (Primary actions, active tab pill)
  - **Cyber Violet**: `#a855f7` (Citation badges, AI indicators)
  - **Emerald Success**: `#10b981` (High semantic relevance indicator, correct quiz answer)
  - **Subtle Slate**: `#94a3b8` (Secondary metadata, citation excerpts)
- **Typography**: Inter (Body) + JetBrains Mono / SFMono (Code snippets, page citations, JSON structures).

---

### 2. Screen Workflows & Component Hierarchy
- **Split Workspace Layout**:
  - **Left Rail (320px width)**: Document Library panel with drag-and-drop file upload target, active document selector, chunk inspection inspector, and index statistics.
  - **Main Viewport (Flex 1)**:
    - **Header**: Document title, page count badge, Mode Switcher Tabs (`[Chat Assistant]`, `[Interactive Quiz]`, `[Document Summary]`).
    - **Chat Mode**: Chronological message feed with rich Markdown rendering. Assistant messages feature interactive citation chips (`[Doc 1, p. 14]`) that open a drawer highlighting the exact source passage.
    - **Quiz Mode**: Clean, distraction-free cards with radio button answer choices, immediate feedback animations, and page references.
    - **Summary Mode**: Three-column structured overview: Executive Summary, Key Formulas & Vocabulary, and High-Yield Revision Points.
