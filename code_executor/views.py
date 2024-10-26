import json
import subprocess
import sys
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def execute_code(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            code = data.get('code', '')

            # Log the received code (optional for debugging)
            print(f"Received code: {code}")

            # Execute the Python code and capture the output
            output = subprocess.check_output(
                [sys.executable, '-c', code],  # Use sys.executable for portability
                stderr=subprocess.STDOUT,
                text=True
            )

            # Log successful output
            print(f"Code executed successfully. Output: {output}")
            return JsonResponse({'output': output, 'error': ''})

        except json.JSONDecodeError:
            # Handle JSON decode error
            return JsonResponse({'output': '', 'error': 'Invalid JSON format'})

        except subprocess.CalledProcessError as e:
            # Capture the specific error message
            print(f"Error executing code: {str(e.output)}")
            return JsonResponse({'output': '', 'error': str(e.output)})

        except Exception as e:
            # Catch-all for any other exceptions
            print(f"Unexpected error: {str(e)}")
            return JsonResponse({'output': '', 'error': 'An unexpected error occurred'})

    return JsonResponse({'output': '', 'error': 'Invalid request'})
