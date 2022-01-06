from django.core.management import call_command
from django.urls import reverse

from rest_framework.test import APITestCase, APIRequestFactory
from repertoire import views
from repertoire.models import File, Work


class CustomerFetchTest(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.url = reverse("repertoire:file-list")
        call_command("load_files_to_db")
        self.file = File.objects.first()
        self.work = Work.objects.first()

    def test_files_loaded_to_db(self):
        """
        Test that the loaded files are in the databse
        """
        files = File.objects.all()
        self.assertTrue(files.exists())

    def test_fetch_files(self):
        """
        Test that fetching all files from database returns succesully and with data
        """
        request = self.factory.get(self.url)
        view = views.FileViewset.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)

    def test_fetch_single_file_by_id(self):
        """
        Test that fetching a single file from database returns succesully and with data
        """
        request = self.factory.get(self.url)
        view = views.FileViewset.as_view({"get": "retrieve"})
        response = view(request, pk=self.file.pk)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)

    def test_create_files(self):
        request = self.factory.post(self.url, data={})
        with self.assertRaises(AttributeError):
            view = views.FileViewset.as_view({"post": "create"})
            response = view(request)
            self.assertEqual(response.status_code, 405)

    def test_get_works_for_a_file(self):
        """
        Test that fetching the works a single file from database returns succesully and with data
        """
        request = self.factory.get(self.url)
        view = views.FileViewset.as_view({"get": "works"})
        response = view(request, pk=self.file.pk)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)

    def test_get_single_works_for_a_file(self):
        """
        Test that fetching a single work for a single file from database returns succesully and with data
        """
        request = self.factory.get(self.url)
        view = views.FileViewset.as_view({"get": "single_works"})
        response = view(request, pk=self.file.pk, work_id=self.work.id)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)