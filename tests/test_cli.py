from click.testing import CliRunner
from hospital.cli import cli


def test_cli_persistence(tmp_path):
    """Test that patients are saved and loaded from file"""
    data_file = tmp_path / "test_data.json"
    runner = CliRunner()
    
    # Add a patient
    result = runner.invoke(cli, ['--data-file', str(data_file),
                               'add', 'Test Patient', '42',
                               '--diagnosis', 'Test Case'])
    assert result.exit_code == 0
    assert 'Added patient' in result.output
    assert str(data_file) in result.output
    
    # List should show the patient
    result = runner.invoke(cli, ['--data-file', str(data_file), 'list'])
    assert result.exit_code == 0
    assert 'Test Patient' in result.output
    assert '42' in result.output
    
    # New CLI instance should load the saved patient
    result = runner.invoke(cli, ['--data-file', str(data_file), 'list'])
    assert result.exit_code == 0
    assert 'Test Patient' in result.output