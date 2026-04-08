# Learning Notes – AI Toolbox

## 1. Prompt Engineering Insights
| Task Type  | Effective Prompt Pattern                       |
|------------|------------------------------------------------|
| Summarizer | "Please summarize in one sentence..."          |
| Polisher   | "Rewrite into a more formal version"           |
| Translator | "Translate to [language], keep meaning"        |
| Classifier | "Categorize into [categories], output as list" |

## 2. Problems & Solutions
- **Problem**: Output sometimes mixes languages
- **Solution**: Specify language clearly in prompt

- **Problem**: Long text input exceeds token limit
- **Solution**: Truncate text or split into chunks before processing

## 3. Future Improvements
- Add GUI interface (using Tkinter or Streamlit)
- Support batch file processing
- Save history to local storage

## 4. Troubleshooting - API Migration
**Problem**: The old `google-generativeai` package was deprecated and returned 404 errors.

**Solution**: Migrated to the new `google-genai` SDK and updated the model name to `gemini-2.0-flash-exp`.

**Lesson learned**: Always check for SDK deprecation warnings and migrate to supported versions.