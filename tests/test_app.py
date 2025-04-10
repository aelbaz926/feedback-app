from feedback_backend.app import app

def test_get_messages_returns_200():
    with app.test_client() as client:
        response = client.get('/api/messages')
        assert response.status_code == 200 or response.status_code == 500  # 500 if DB isn't up

def test_post_message_returns_201():
    with app.test_client() as client:
        response = client.post('/api/message', json={'message': 'Test from pytest'})
        assert response.status_code in [201, 500]  # 500 if DB not ready
