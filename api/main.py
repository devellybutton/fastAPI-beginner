from fastapi import FastAPI

app = FastAPI()

courses = {
	1: {
		"title": "Modern History",
		"teacher": "Ms.Doe",
		"students": ["Harry Potter", "Frodo Baggins"],
		"level": "advanced"
	},
	2: {
		"course": "Mathematics",
		"teacher": "Mr. Davies",
		"students": ["John Smith", "Bruce Lee"],
		"level": "beginner"
	},
	3: {
		"title": "Geography",
		"teacher": "Mr. Apple",
		"students": ["Michael Jordan", "Bruce Lee"],
		"level": "advanced"
	}
}

@app.get("/api/hello/")
def hello_word():
    return {"message": "Hello World"}

@app.get("/api/courses")
def get_courses():
    return courses