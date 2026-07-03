from flask import Flask, render_template, request
import re
import pdfplumber


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/analyze", methods=["GET","POST"])
def analyze():
    try:
        file = request.files["resume"]
        skills_input = request.form["skills"]

        # Optional safety checks
        if file.filename == "":
            return "❌ No file selected"
        

        resume_data=""

        # 🔹 Handle TXT files
        if file.filename.endswith(".txt"):
            resume_data = file.read().decode("utf-8")

        # 🔹 Handle PDF files
        elif file.filename.endswith(".pdf"):
            with pdfplumber.open(file) as pdf_file:
                for page in pdf_file.pages:#[page-1,page-2]
                    text = page.extract_text()
                    if text:
                        resume_data += text

        else:
            return "❌ Only .txt and .pdf allowed"


        # Convert to lowercase

        resume_data = resume_data.lower()
        # Step 2: Skills input
        skills_input = skills_input.lower() #["python","mysql","  flask"," java ",javascript"]
        required_skills = [skill.strip() for skill in skills_input.split(",")] #["python","mysql","flask","java","javascript"]

        total_skills = len(required_skills)
        matched_skills = 0
        non_matched_skills=0
        matched = []
        n_matched=[]



        # Step 3: Matching
        for skill in required_skills:#["python","mysql","flask","java","javascript"]
            #pattern = r"\b" + re.escape(skill) + r"\b"
            pattern_1=r"(?<!\w)"  + re.escape(skill) + r"(?!\w)" 
          

            if re.search(pattern_1, resume_data):
                matched.append((skill, "✅ Found"))
                matched_skills += 1
            else:
                n_matched.append((skill, "❌ Not Found"))
                non_matched_skills+=1

        # FIX 2: Correct indentation (was outside loop incorrectly)
        # Step 4: Score
        score = (matched_skills / total_skills) * 100 if total_skills > 0 else 0


        # Step 5: Result
        if score > 90 and score<=100:
            status = "🔥 Priority Candidate"

        elif score >= 70 and score <90 :
            status = "✅ Shortlisted"


        else:
            status = "❌ Not Selected"



        
        return render_template("result.html",score=score,matched=matched,n_matched=n_matched,matched_skills=matched_skills,non_matched_skills=non_matched_skills,status=status)


    except Exception as e:
        return f"Error: {e}"

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)


