from fastapi import FastAPI, HTTPException, status
from typing import Union

app = FastAPI()

# 프로그램 실행시에 courses가 정의되기 때문에
# 만약 삭제한다고 해도 서버 재실행시에 다시 생성됨.
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

@app.get("/api/courses/")
def get_courses(level: Union[str, None] = None):
    if level:
        level_course = []
        for index in courses.keys():
            if courses[index]["level"] == level:
                level_course.append(courses[index])
        return level_course
    return courses

@app.get("/api/courses/{course_id}/")
def get_courses(course_id: int):
    try:
        return courses[course_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Course with id: {course_id} was not found!"
        )

@app.delete("/api/courses/{course_id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(course_id: int):
    try:
        del courses[course_id]
        return {"message": f"Course with id {course_id} has been deleted."}
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Course with id: {course_id} was not found!"
        )