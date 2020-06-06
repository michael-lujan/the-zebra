import pytest
import os

@pytest.fixture
def test_schema_csv_file():
    test_csv_path = 'test_schema.csv'
    lines = [
        'name,type,is_nullable,version',
        'test 1,String,Yes,1',
        'test-2,String,No,1',
        'test_3,Float,Yes,1',
        'test4,Float,No,1']
    _write_file_to_disk(test_csv_path, lines)
    yield test_csv_path, lines
    _remove_file_from_disk(test_csv_path)

@pytest.fixture
def test_schema():
    test_schema = [
        {'name': 'test 1', 'type': 'String', 'is_nullable': True, 'version': '1'},
        {'name': 'test-2', 'type': 'String', 'is_nullable': False, 'version': '1'},
        {'name': 'test_3', 'type': 'Float', 'is_nullable': True, 'version': '1'},
        {'name': 'test4', 'type': 'Float', 'is_nullable': False, 'version': '1'}]
    yield test_schema

@pytest.fixture
def test_schema_match_csv_file():
    test_csv_path = 'test_home_insurance.csv'
    lines = [
        'test 1,test-2,test_3,test4',
        'hi,red,3,4',
        ',red,3,4',
        'hi,,3,4',
        'hi,red,,4',
        'hi,red,3,']
    _write_file_to_disk(test_csv_path, lines)
    yield test_csv_path, lines
    _remove_file_from_disk(test_csv_path)

@pytest.fixture
def test_schema_match_records():
    return [
        {'test 1': 'hi', 'test-2': 'red', 'test_3': 3.0, 'test4': 4.0},
        {'test 1': None, 'test-2': 'red', 'test_3': 3.0, 'test4': 4.0},
        {'test 1': 'hi', 'test-2': 'red', 'test_3': None, 'test4': 4.0}]

@pytest.fixture
def test_schema_included_csv_file():
    test_csv_path = 'test_home_insurance.csv'
    lines = [
        'test 1,test-2,test_3,test4,test_extra1,test_extra2',
        'hi,red,3,4,test,test',
        ',red,3,4,test,test',
        'hi,,3,4,test,test',
        'hi,red,,4,test,test',
        'hi,red,3,,test,test']
    _write_file_to_disk(test_csv_path, lines)
    yield test_csv_path, lines
    _remove_file_from_disk(test_csv_path)

@pytest.fixture
def test_schema_included_records():
    return [
        {'test 1': 'hi', 'test-2': 'red', 'test_3': 3.0, 'test4': 4.0},
        {'test 1': None, 'test-2': 'red', 'test_3': 3.0, 'test4': 4.0},
        {'test 1': 'hi', 'test-2': 'red', 'test_3': None, 'test4': 4.0}]

@pytest.fixture
def test_schema_mismatch_csv_file():
    test_csv_path = 'test_home_insurance.csv'
    lines = [
        'test_a,test_b,test_c,test_d',
        'hi,red,3,4',
        ',red,3,4',
        'hi,,3,4',
        'hi,red,,4',
        'hi,red,3,']
    _write_file_to_disk(test_csv_path, lines)
    yield test_csv_path, lines
    _remove_file_from_disk(test_csv_path)

@pytest.fixture
def test_schema_mismatch_records():
    return []

@pytest.fixture
def test_home_insurance_csv_file():
    test_csv_path = 'test_home_insurance.csv'
    lines = [
        'Provider Name,CampaignID,Phone Number,Redirect Link,Zipcode,Address,Cost Per Ad Click,TestColumn',
        'Home R'' Us,HOME,1234567,homerus.com,"""78705""",Tim Street,5,testColumn',
        'HomeGuard,HOME1,1234567,homeguard.com,"""78705""",Tam Street,5.5,testColumn',
        'WeProtect,HOME2,1234567,weprotect.com,"""78705""",,6,testColumn',
        'HomesOnly,HOME3,,homesonly.com,"""78705""",6th Street,5,testColumn',
        'Homes4U,HOME5,1234567,homes4u.com,"""78705""",North Pole,6,testColumn']
    _write_file_to_disk(test_csv_path, lines)
    yield test_csv_path, lines
    _remove_file_from_disk(test_csv_path)

@pytest.fixture
def test_pet_insurance_csv_file():
    test_csv_path = 'test_pet_insurance.csv'
    lines = [
        'Provider Name,CampaignID,Phone Number,Redirect Link,Zipcode,Address',
        'Pet R'' Us,HOME,1234567,homerus.com,"""78715""",Tim Street',
        'PetGuard,HOME1,1234567,homeguard.com,"""78725""",Tam Street',
        'WeProtectPets,HOME2,1234567,weprotect.com,"""78735""",',
        'PetsOnly,HOME3,,homesonly.com,"""78745""",6th Street',
        'Pets4U,HOME5,1234567,homes4u.com,"""78755""",North Pole']
    _write_file_to_disk(test_csv_path, lines)
    yield test_csv_path, lines
    _remove_file_from_disk(test_csv_path)

def _write_file_to_disk(path, lines):
    with open(path, 'w') as f:
        f.write('\n'.join(lines))

def _remove_file_from_disk(path):
    os.remove(path)

