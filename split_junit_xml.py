import xml.etree.ElementTree as ET
import sys

def split_junitxml(input_file: str, output_file: str):
    # Parse the input XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Create a new root element for the output XML
    new_root = ET.Element('testsuites')

    # Group tests by class name
    tests_by_class = {}
    for testcase in root.findall('.//testcase'):
        class_name = testcase.get('classname')
        if class_name not in tests_by_class:
            tests_by_class[class_name] = []
        tests_by_class[class_name].append(testcase)

    # Create a new testsuite element for each class
    for class_name, testcases in tests_by_class.items():
        testsuite = ET.SubElement(new_root, 'testsuite')
        testsuite.set('name', class_name)
        testsuite.set('tests', str(len(testcases)))
        failures = sum(1 for testcase in testcases if testcase.find('failure') is not None)
        testsuite.set('failures', str(failures))
        skipped = sum(1 for testcase in testcases if testcase.find('skipped') is not None)
        testsuite.set('skipped', str(skipped))

        # Calculate total time and errors
        total_time = sum(float(testcase.get('time', '0')) for testcase in testcases)
        errors = sum(1 for testcase in testcases if testcase.find('error') is not None)
        testsuite.set('time', str(total_time))
        testsuite.set('errors', str(errors))

        # Add testcases to the testsuite
        for testcase in testcases:
            testsuite.append(testcase)

    # Write the new XML tree to the output file
    new_tree = ET.ElementTree(new_root)
    new_tree.write(output_file, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python split_junit_xml.py input.xml output.xml")
        sys.exit(1)

    split_junitxml(sys.argv[1], sys.argv[2])
    print(f"✅ Split JUnit XML written to {sys.argv[2]}")
