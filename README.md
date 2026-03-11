# Text to SQL Generator

A natural language to SQL query converter powered by Google's Gemini AI. This application allows users to ask questions in plain English and automatically converts them into SQL queries to retrieve data from a SQLite database.

## 🌟 Features

- **Natural Language Processing**: Convert English questions into SQL queries using Google Gemini 2.5 Flash
- **Interactive Web Interface**: User-friendly Streamlit-based interface
- **Real-time Query Execution**: Execute generated SQL queries and display results instantly
- **Student Database**: Pre-populated SQLite database with student records
- **Environment-based Configuration**: Secure API key management using environment variables

## 📋 Prerequisites

- Python 3.8+
- Google Gemini API key

## 🚀 Installation

1. **Clone or download the project**
   ```bash
   cd text_to_sql_generator
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the project root directory
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_gemini_api_key_here
     ```

5. **Initialize the database**
   ```bash
   python sqlite.py
   ```
   This creates a `student.db` SQLite database with sample student records.

## 📖 Usage

1. **Start the Streamlit application**
   ```bash
   streamlit run sql.py
   ```

2. **Open your browser**
   - The application will open automatically at `http://localhost:8501`

3. **Enter your question**
   - Type a natural language question about the student database
   - Example: "How many students are in Data Science class?"

4. **View results**
   - The application will convert your question to SQL and display the results

## 📚 Example Queries

- "How many entries of records are present?" 
  - Converts to: `SELECT COUNT(*) FROM STUDENT;`

- "Tell me all the students studying in Data Science class?"
  - Converts to: `SELECT * FROM STUDENT WHERE CLASS='Data Science';`

- "Show me students with marks greater than 90"
  - Converts to: `SELECT * FROM STUDENT WHERE MARKS > 90;`

## 🗄️ Database Schema

The application uses a SQLite database with the following structure:

**Table: STUDENT**
| Column   | Type        | Description              |
|----------|-------------|--------------------------|
| NAME     | VARCHAR(25) | Student's full name      |
| CLASS    | VARCHAR(25) | Class/Program name       |
| SECTION  | VARCHAR(25) | Section/Group identifier |
| MARKS    | INT         | Student's marks/score    |

### Sample Data

The database includes 5 sample records:
- Krish (Data Science, Section A, 90 marks)
- Sudhanshu (Data Science, Section B, 85 marks)
- Parth (Data Science, Section A, 88 marks)
- Kamo (DEVOPS, Section A, 92 marks)
- Neel (DEVOPS, Section A, 87 marks)

## 📁 Project Structure

```
text_to_sql_generator/
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
├── sql.py             # Main Streamlit application
├── sqlite.py          # Database initialization script
├── student.db         # SQLite database (created after running sqlite.py)
└── .env              # Environment variables (create this file)
```

## 🔧 Dependencies

- **streamlit**: Web application framework for data apps
- **google-generativeai**: Google Gemini API client library
- **python-dotenv**: Load environment variables from .env file
- **sqlite3**: Built-in Python SQLite library

## ⚙️ Configuration

### API Key Setup
1. Get your Google Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create a `.env` file in the project root
3. Add: `GOOGLE_API_KEY=your_key_here`

### Database Setup
The `sqlite.py` script automatically:
- Creates a SQLite database named `student.db`
- Creates the STUDENT table with columns: NAME, CLASS, SECTION, MARKS
- Inserts 5 sample student records
- Commits and closes the database connection

## 🤖 AI Model

This application uses **Google Gemini 2.5 Flash**, a state-of-the-art language model that:
- Understands natural language questions
- Converts them to accurate SQL queries
- Provides context-aware responses

## 📝 Notes

- The SQL prompt is pre-configured for the STUDENT table
- The AI is instructed to return clean SQL without backticks or the word "SQL"
- Modify the `prompt` variable in `sql.py` to customize for different database schemas
- For production use, consider adding input validation and error handling

## 🔒 Security

- API keys are managed through environment variables and not hardcoded
- Use `.gitignore` to prevent `.env` file from being committed
- Keep your Google API key confidential

## 📦 Libraries Used

| Library | Purpose |
|---------|---------|
| streamlit | Web UI framework |
| google-generativeai | Gemini API integration |
| python-dotenv | Environment variable management |
| sqlite3 | Database operations |

## 🎯 Future Enhancements

- Support for multiple database schemas
- Query history and favorites
- SQL query validation and optimization
- Role-based access control
- Multi-language support

## 💡 Troubleshooting

**Issue: "API key not found"**
- Ensure `.env` file exists in the project root
- Verify `GOOGLE_API_KEY` is correctly set

**Issue: "student.db not found"**
- Run `python sqlite.py` to initialize the database

**Issue: Streamlit not starting**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify you're in the correct project directory

## 📄 License

This project is open source and available for educational and development purposes.

---

**Built with ❤️ using Streamlit and Google Gemini AI**