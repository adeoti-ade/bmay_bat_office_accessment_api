from django.core.management.base import BaseCommand
from django.db import transaction
from repertoire.models import File, Work
from repertoire.utils import parse_file



class Command(BaseCommand):
    help = 'Create Works'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        files, processed_works = self.process_files()
        files_qs = [File(**obj) for obj in files]
        File.objects.bulk_create(files_qs)
        works_qs = [Work(**obj) for obj in processed_works]
        Work.objects.bulk_create(works_qs)
        self.stdout.write(f"loaded {len(files)} files and {len(processed_works)} works")

    def process_files(self):
        file_array = parse_file()
        files = []
        works = []
        for file in file_array:
            files.append(
                {
                    "work_count": file["work_count"],
                    "filename": file["filename"]
                }
            )
            works.append(
                file["works"]
            )
        flat_works = [item for sublist in works for item in sublist]
        processed_works = []
        for item in flat_works:
            item["contributors"] = item["contributors"].split("|")
            processed_works.append(item)

        return files, processed_works