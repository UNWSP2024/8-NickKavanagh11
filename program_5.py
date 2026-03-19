# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

def main():
    courses = []

    while True:
        course_id = input("Enter course ID (or 'done' to finish): ")
        if course_id.lower() == "done":
            break

        course_name = input("Enter course name: ")
        courses.append((course_id, course_name))

    subject = input("Enter subject to search for (e.g., COS): ")

    print("\nMatching Courses:")
    for course_id, course_name in courses:
        if course_id.upper().startswith(subject.upper()):
            print(course_id, "-", course_name)

if __name__ == "__main__":
    main()
