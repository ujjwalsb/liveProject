'''

curl -X POST -d "username=ujjwalsb&password=usbx9rcp" http://127.0.0.1:8000/api/auth/token/

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVqandhbHNiIiwidXNlcl9pZCI6MSwiZW1haWwiOiJ1amp3YWxAZ21haWwuY29tIiwiZXhwIjoxNTIzODcwNTg0fQ.4fxrhukYUz2zPgfDTuxajbvQHb4bjOuDmrnVu02fchs
curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVqandhbHNiIiwidXNlcl9pZCI6MSwiZW1haWwiOiJ1amp3YWxAZ21haWwuY29tIiwiZXhwIjoxNTIzODcwNTg0fQ.4fxrhukYUz2zPgfDTuxajbvQHb4bjOuDmrnVu02fchs" http://127.0.0.1:8000/api/comments
curl http://127.0.0.1:8000/api/comments


curl -X POST -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVqandhbHNiIiwidXNlcl9pZCI6MSwiZW1haWwiOiJ1amp3YWxAZ21haWwuY29tIiwiZXhwIjoxNTIzODcxMDIyfQ.4V20v1r5lAlHeSIVmui8JLGGmvRBBn8uQ2hKRv8OXxc" -H "Content-Type: application/json" -d '{"content": "curl comment"}' http://127.0.0.1:8000/api/comments/create/?type=post&slug=melting-iron-man



'''
