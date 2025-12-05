from unittest.mock import MagicMock, patch
import exp6_db_script # Student file

@patch('mysql.connector.connect')
def test_database_connection(mock_connect):
    # Run student function
    exp6_db_script.run_db_operations()

    # Assert connection was attempted [cite: 435]
    mock_connect.assert_called_with(
        host="localhost", user="root", password="password", database="company_db"
    )

def test_create_table_query():
    # Mock the cursor to capture executed SQL
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    with patch('mysql.connector.connect', return_value=mock_conn):
        exp6_db_script.run_db_operations()

        # Check if CREATE TABLE was called [cite: 436]
        # We search through all calls to execute()
        found_create = False
        for call in mock_cursor.execute.call_args_list:
            if "CREATE TABLE" in call[0][0]:
                found_create = True
                break
        assert found_create, "CREATE TABLE SQL query was not executed"