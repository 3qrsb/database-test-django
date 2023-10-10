
from django.test import TestCase
from django.urls import reverse
from student.models import Student

"""
---UNIT TEST---

class StudentViewsTestCase(TestCase):

    def setUp(self):
        # Create a sample student for testing
        self.student = Student.objects.create(name='John', section='A', age=20)

    def test_student_list_view(self):
        response = self.client.get(reverse('student:student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/student_list.html')

    def test_student_create_view(self):
        data = {'name': 'Alice', 'section': 'B', 'age': 22}
        response = self.client.post(reverse('student:student_new'), data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertEqual(Student.objects.count(), 2)  # Assuming one student already exists

    def test_student_update_view(self):
        updated_data = {'name': 'Updated Name', 'section': 'C', 'age': 25}
        response = self.client.post(reverse('student:student_edit', args=[self.student.pk]), updated_data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.student.refresh_from_db()
        self.assertEqual(self.student.name, 'Updated Name')
        self.assertEqual(self.student.section, 'C')
        self.assertEqual(self.student.age, 25)

    def test_student_delete_view(self):
        response = self.client.post(reverse('student:student_delete', args=[self.student.pk]))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertFalse(Student.objects.filter(pk=self.student.pk).exists())

---INTEGRATION TEST---

class StudentViewsIntegrationTestCase(TestCase):

    def test_student_crud_workflow(self):
        # Create a student
        create_url = reverse('student:student_new')
        data = {'name': 'Alice', 'section': 'A', 'age': 22}
        response = self.client.post(create_url, data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertEqual(Student.objects.count(), 1)

        # Retrieve the created student
        student = Student.objects.first()
        self.assertEqual(student.name, 'Alice')
        self.assertEqual(student.section, 'A')
        self.assertEqual(student.age, 22)

        # Update the student
        update_url = reverse('student:student_edit', args=[student.pk])
        updated_data = {'name': 'Updated Alice', 'section': 'B', 'age': 25}
        response = self.client.post(update_url, updated_data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        student.refresh_from_db()
        self.assertEqual(student.name, 'Updated Alice')
        self.assertEqual(student.section, 'B')
        self.assertEqual(student.age, 25)

        # Delete the student
        delete_url = reverse('student:student_delete', args=[student.pk])
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertFalse(Student.objects.filter(pk=student.pk).exists())

---SMOKE TEST---

class SmokeTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name="Test Student", section="A", age=20)

    def test_student_list_view(self):
        response = self.client.get(reverse('student:student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.student.name)

    def test_student_create_view(self):
        data = {
            'name': 'New Student',
            'section': 'B',
            'age': 21
        }
        response = self.client.post(reverse('student:student_new'), data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertTrue(Student.objects.filter(name='New Student').exists())

    def test_student_update_view(self):
        data = {
            'name': 'Updated Student',
            'section': 'C',
            'age': 22
        }
        response = self.client.post(reverse('student:student_edit', args=[self.student.pk]), data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.student.refresh_from_db()
        self.assertEqual(self.student.name, 'Updated Student')
        self.assertEqual(self.student.section, 'C')
        self.assertEqual(self.student.age, 22)

    def test_student_delete_view(self):
        response = self.client.post(reverse('student:student_delete', args=[self.student.pk]))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertFalse(Student.objects.filter(pk=self.student.pk).exists())

    def tearDown(self):
        self.student.delete() 
"""
class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="John Doe",
            section="A",
            age=20
        )

    def test_student_creation(self):
        self.assertEqual(self.student.name, "John Doe")
        self.assertEqual(self.student.section, "A")
        self.assertEqual(self.student.age, 20)

    def test_student_absolute_url(self):
        expected_url = reverse('student:student_edit', kwargs={'pk': self.student.pk})
        self.assertEqual(self.student.get_absolute_url(), expected_url)

class StudentListViewTestCase(TestCase):
    def test_student_list_view(self):
        response = self.client.get(reverse('student:student_list'))
        self.assertEqual(response.status_code, 200)
        # You can add more assertions here to check the content of the response.

class StudentCreateViewTestCase(TestCase):
    def test_student_create_view(self):
        response = self.client.post(reverse('student:student_new'), data={
            'name': 'New Student',
            'section': 'B',
            'age': 22,
        })
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect

        # Check if the student was created in the database
        self.assertTrue(Student.objects.filter(name='New Student', section='B', age=22).exists())

class StudentUpdateViewTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="John Doe",
            section="A",
            age=20
        )

    def test_student_update_view(self):
        response = self.client.post(reverse('student:student_edit', kwargs={'pk': self.student.pk}), data={
            'name': 'Updated Student',
            'section': 'C',
            'age': 25,
        })
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect

        # Check if the student was updated in the database
        updated_student = Student.objects.get(pk=self.student.pk)
        self.assertEqual(updated_student.name, 'Updated Student')
        self.assertEqual(updated_student.section, 'C')
        self.assertEqual(updated_student.age, 25)

class StudentDeleteViewTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="John Doe",
            section="A",
            age=20
        )

    def test_student_delete_view(self):
        response = self.client.post(reverse('student:student_delete', kwargs={'pk': self.student.pk}))
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect

        # Check if the student was deleted from the database
        self.assertFalse(Student.objects.filter(pk=self.student.pk).exists())
