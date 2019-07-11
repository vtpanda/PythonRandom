import json
import base64

def lambda_handler(event, context):
    # TODO implement
    output = []
    succeeded_record_cnt = 0
    failed_record_cnt = 0
    dropped_record_cnt = 0

    for record in event['records']:

        try:

            payload = json.loads(base64.b64decode(record['data']).decode('utf-8'))

            succeeded_record_cnt += 1

            if payload['results'][0]['dob']['age'] >= 21:
                data_field = {
                    'firstname': payload['results'][0]['name']['first'],
                    'lastname': payload['results'][0]['name']['last'],
                    'age': payload['results'][0]['dob']['age'],
                    'gender': payload['results'][0]['gender'],
                    'latitude': payload['results'][0]['location']['coordinates']['latitude'],
                    'longitude': payload['results'][0]['location']['coordinates']['longitude']
                }

                output_record = {
                    'recordId': record['recordId'],
                    'result': 'Ok',
                    'data': base64.b64encode((json.dumps(data_field) + '\n').encode('utf-8')).decode('utf-8')
                }

            else:
                print('Dropped Record: Age < 21')
                dropped_record_cnt += 1
                output_record = {
                    'recordId': record['recordId'],
                    'result': 'Dropped',
                    'data': record['data']
                }
        except json.JSONDecodeError:
            print('Processing failed: Not a valid JSON Document')
            failed_record_cnt += 1
            output_record = {
                'recordId': record['recordId'],
                'result': 'ProcessingFailed',
                'data': record['data']
            }
        except Exception as e:
            print('Processing failed: Unknown Reason')
            print (e)
            failed_record_cnt += 1
            output_record = {
                'recordId': record['recordId'],
                'result': 'ProcessingFailed',
                'data': record['data']
            }
        output.append(output_record)

    print('Processing completed.  Successful records {}, Dropped records {}, Failed records {}.'.format(succeeded_record_cnt, dropped_record_cnt, failed_record_cnt))
    return {'records': output}
