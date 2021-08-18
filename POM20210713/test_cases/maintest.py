import pytest
from test_cases.sendmessage import send_email

if __name__ == '__main__':
    pytest.main(['-s', '-v'])
    file_new = './report/report.html'
    send_email(file_new)
