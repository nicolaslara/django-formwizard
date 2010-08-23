from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDict
from django.http import QueryDict
from formwizard.storage.session import SessionStorage

class UploadsStorage(SessionStorage):
    def __init__(self, prefix, request, *args, **kwargs):
        self.file_storage = FileSystemStorage()
        super(UploadsStorage, self).__init__(prefix, request, *args, **kwargs)

    def set_step_data(self, step, cleaned_data):
        """
        This is currently based on ssession, but should be abstracted
        to work with any storage
        """
        files = cleaned_data.get('files', None)
        del cleaned_data['files']
        if files:
            #setting the format straight
            cleaned_data._mutable = True        
            cleaned_data.setlist('files', files)
            cleaned_data._mutable = False        
            print cleaned_data
        return super(UploadsStorage, self).set_step_data(step, cleaned_data)

    def get_files(self):
        files = MultiValueDict({})
        for step, step_data in self.request.session[self.prefix][self.step_data_session_key].items():
            if step_data.has_key('files'):
                for file in step_data.getlist('files'):
                    files.appendlist(step+'-file', self.file_storage.open(file.get('path')))
        return files
