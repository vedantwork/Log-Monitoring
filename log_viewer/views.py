from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
from django.http import HttpResponse
import traceback

class LogView(View):
    def get(self, request):
        # declaring a constant error log file in setting so that just by import it can be used anywhere in our project
        log_file_path = settings.LOG_FILE_PATH  
        print("log_file_path ====>>>> ",log_file_path)
        context = {'log_lines': self.get_me_error_lines(log_file_path)}
        print("context ====>>>> ",context)
        return render(request, 'log_viewer/log.html', context)
    
    def get_me_error_lines(self, file_path, num_lines=10):
        lines = []
        try:
            with open(file_path, 'r') as file:
                if lines is not None:
                    all_lines = file.readlines()
                    lines = all_lines[-num_lines:]
        except FileNotFoundError:
            print(f"File not found =====>>>> ",file_path)
        except PermissionError:
            print(f"Permission error =====>>>>> ",file_path)
        except Exception as e:
            print("traceback error ====>>> ",traceback.format_exc())
            print(f"Error occured while reading the log file ====>>>> ",e)
            # return HttpResponse(traceback.format_exc())
        return lines
    
