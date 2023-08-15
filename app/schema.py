import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django.db.models import Avg 
from .models import Student, Course, Score

class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        exclude=('id',)
    
class CreateStudent(graphene.Mutation):
    class Arguments:
        student_id = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
    
    success = graphene.Boolean()
    student = graphene.Field(StudentType)
    message = graphene.String()

    def mutate(self, info, student_id, first_name, last_name):
        try:
            student = Student(
                student_id=student_id,
                first_name=first_name,
                last_name=last_name,
            )
            student.save()
            return CreateStudent(
                success=True,
                student=student,
                message=f"Created"
            )
        except:
            return CreateStudent(
                success=False,
                student=None,
                message=f"Failed"
            )
    
# class CreateStudentType(graphene.InputObjectType):
#     student_id = graphene.String(required=True)
#     first_name = graphene.String()
#     last_name = graphene.String()

# class CreateStudents(graphene.Mutation):
#     class Arguments:
#         students_data = graphene.List(graphene.NonNull(CreateStudentType))
    
#     success = graphene.Boolean()
#     message = graphene.String()
#     students = graphene.List(graphene.NonNull())

#     def mutate(self, info, students_data):
#         students = []

#         for student_data in students_data:
#             try:
#                 student = Student(student_data)
#                 students.append(student)
#             except:
#                 return CreateStudents(success=False, message=f"Failed to create student with data=<{student_data}>")

#         for i in range(len(students)):
#             try:
#                 students[i].save()
#             except:
#                 for j in range(i-1, -1, -1):
#                     students[j].delete()
#                 return CreateStudents(success=False, message=f"Failed to save students in database")
        
#         return CreateStudents(success=True, message="Created all students")

class UpdateStudent(graphene.Mutation):
    class Arguments:
        student_id = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String(required=True)

    success = graphene.Boolean()
    student = graphene.Field(StudentType)
    message = graphene.String()

    def mutate(self, info, student_id, first_name, last_name):
        try:
            student = Student.objects.get(student_id=student_id)
            if not first_name or not last_name:
                raise ValueError("haha")
            student.first_name = first_name
            student.last_name = last_name
            student.save()
            return UpdateStudent(
                success=True,
                student=student,
                message=f"Updated successfully"
            )
        except:
            return UpdateStudent(
                student=None,
                message=f"Student with student_id '{student_id}' does not exist."
            )
        
class DeleteStudent(graphene.Mutation):
    class Arguments:
        student_id = graphene.String(required=True)
    
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, student_id):
        try:
            student = Student.objects.get(student_id=student_id)
            student.delete()
            return DeleteStudent(
                success=True,
                message=f"deleted"
            )
        except:
            return DeleteStudent(
                success=False,
                message=f"not found",
            )

class CourseType(DjangoObjectType):
    class Meta:
        model = Course
        fields = '__all__'

class CreateCourse(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    success = graphene.Boolean()
    course = graphene.Field(CourseType)
    message = graphene.String()

    def mutate(self, info, name):
        try:
            course = Course(name=name)
            course.save()
            return CreateCourse(course=course, message=f"Created")
        except:
            return CreateCourse(course=None, message=f"Failed")

class UpdateCourse(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        new_name = graphene.String()
    
    success = graphene.Boolean()
    course = graphene.Field(CourseType)
    message = graphene.String()

    def mutate(self, info, name, new_name):
        try:
            course = Course.objects.get(name=name)
            course.name = new_name
            course.save()
            return UpdateCourse(
                success=True,
                course=course,
                message="Created",
            )
        except:
            return UpdateCourse(
                success=False,
                course=None,
                message="Failed",
            )
        
class DeleteCourse(graphene.Mutation):
    class Arguments:
        name = graphene.String()
    
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, name):
        try:
            course = Course.objects.get(name=name)
            course.delete()
            return DeleteCourse(
                success=True,
                message="Deleted"
            )
        except:
            return DeleteCourse(
                success=False,
                message="Failed"
            )

class ScoreType(DjangoObjectType):
    class Meta:
        model = Score
        # fields = '__all__'
        exclude=('id',)

class CreateScore(graphene.Mutation):
    class Arguments:
        student_id = graphene.String()
        course_name = graphene.String()
        value = graphene.Decimal()
    
    success = graphene.Boolean()
    score = graphene.Field(ScoreType)
    message = graphene.String()

    def mutate(self, info, student, course_name, value):
        try:
            score = Score(student=student, course_name=course_name)
            score.save()
            return CreateScore(
                success=True,
                score=score,
                message="Created",
            )
        except:
            return CreateScore(
                success=True,
                score=score,
                message="Failed",
            )
    
class DeleteScore(graphene.Mutation):
    class Arguments:
        student_id = graphene.String()
        course_id = graphene.String()
    
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, student_id, course_id):
        try:
            score = Score.objects.get(
                student_id=student_id,
                course_id=course_id,
            )
            score.delete()
            return DeleteScore(
                success=True,
                message=f"Deleted"
            )
        except:
            return DeleteScore(
                success=False,
                message=f"Failed"
            )

class Query(graphene.ObjectType):
    student = graphene.Field(
        StudentType,
        student_id=graphene.String()
    )
    all_students = graphene.List(StudentType)

    course = graphene.Field(
        CourseType,
        name=graphene.String()
    )
    all_courses = graphene.List(StudentType)

    score = graphene.Field(
        ScoreType,
        student_id=graphene.String(),
        course_id=graphene.String(),
    )
    all_scores = graphene.List(ScoreType)
    average_score = graphene.Float(course_name=graphene.String(required=True))

    def resolve_student(self, info, student_id):
        try:
            return Student.objects.get(student_id=student_id)
        except Student.DoesNotExist:
            return None

    def resolve_all_students(self, info):
        return Student.objects.all()

    def resolve_all_courses(self, info):
        return Course.objects.all()

    def resolve_all_scores(self, info):
        return Score.objects.all()
    
    def resolve_average_score(self, info, course_name):
        try:
            course = Course.objects.get(name=course_name)
            average_score = Score.objects.filter(course=course).aggregate(Avg('value'))['value__avg']
            return average_score
        except Course.DoesNotExist:
            return None
    
class Mutation(graphene.ObjectType):
    create_student = CreateStudent.Field()
    # create_students = CreateStudents.Field()
    update_student = UpdateStudent.Field()
    delete_student = DeleteStudent.Field()
    update_course = UpdateCourse.Field()
    

# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query, mutation=Mutation)
