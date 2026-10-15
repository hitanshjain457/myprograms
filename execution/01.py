class Student:
  def __init__(self, roll_no, name, marks):
    self.roll_no = roll_no
    self.name = name
    self.marks = marks
class ClassRoom:
  def __init__(self, students_list=None):
    self.students_list =  []
  def get_unique_subjects(self):
    unique_subjects = set()
    for student in self.students_list:
      unique_subjects.update(student.marks.keys())
    return unique_subjects
  def get_top_performers(self):
    unique_subjects = self.get_unique_subjects()
    top_performers = []
    for subject in unique_subjects:
      top_student_name = None
      highest_score =0
      for student in self.students_list:
        if subject in student.marks:
          score = student.marks[subject]
          if score > highest_score:
            highest_score = score
            top_student_name = student.name
      if top_student_name is not None:
        top_performers.append((subject, top_student_name, highest_score))
    return top_performers
  def remove_duplicate_students(self):
    seen_roll_nos = set()
    clean_list = []
    for student in self.students_list:
      if student.roll_no not in seen_roll_nos:
        seen_roll_nos.add(student.roll_no)
        clean_list.append(student)
    self.students_list = clean_list