
'''
n���� Queen�� ��ġ�ϴ� ����� ���� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.
N-Queen n x n �� ü�� �ǿ� n���� Queen�� ������ �մϴ�. �� ��, ������ ��Ģ�� �ݵ�� ����� �մϴ�.
���� �࿡ 2�� �̻��� Queen�� �����ؼ��� �ȵ˴ϴ�.
���� ���� 2�� �̻��� Queen�� �����ؼ��� �ȵ˴ϴ�.
�ϳ��� �밢���� 2�� �̻��� Queen�� �����ؼ��� �ȵ˴ϴ�. �̴� ��\�� ������ �밢���� ��/�� ������ �밢�� ��ο� ���Ͽ� �ش�Ǵ� �����Դϴ�.
���� ��� n = 4 �� ���, �Ʒ��� ���� Queen�� ��ġ�ϴ� ���� �������� �ʴ�.

first �ֳ��ϸ� ������ ���� ���� 1, �׸��� ���� 3�� ���ϱ� �����̴�.

second n = 4 �� ��쿡�� ������ ���� Queen �� ��ġ�� �� �ִ� ��찡 2���� �����Ѵ�.

third n�� �־��� ��, n���� Queen�� ��ġ�� �� �ִ� ����� ���� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.

�Է� ���� 1
4

��� ���� 1
2

�Է� ���� 2
5

��� ���� 2
10

��Ʈ) itertools�� ����� permutations()�Լ��� ����ϸ� for���� ������� �ʰ��� ������ ���� �� �ֽ��ϴ�.
from itertools import permutations
p = ['a', 'b', 'c']
perm = permutations(p)
print(list(perm))
# ��� ���
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

���� ����
���� ������ �ִ� 10���Դϴ�.
'''
import sys
sys.setrecursionlimit(100000)

def nQueen(n) :

    return 0

def main():
    '''
    �� �κ��� �������� ������.
    '''

    n = int(input())

    print(nQueen(n))

if __name__ == "__main__":
    main()


#elice_utils.py
import base64
import mimetypes
import os
import urllib.parse
import urllib.request

EXECUTION_TOKEN = os.getenv('EXECUTION_TOKEN')
EXECUTOR_IP = os.getenv('EXECUTOR_IP')
EXECUTOR_COM_PORT = os.getenv('EXECUTOR_COM_PORT')

if not all((EXECUTION_TOKEN, EXECUTOR_IP, EXECUTOR_COM_PORT)):
    raise Exception('Invalid elice environment.')

_OTP_KEY = None


def _send(url, data):
    data_encoded = urllib.parse.urlencode(data)
    q = urllib.request.Request(url,
                               data=data_encoded.encode('utf-8'))

    try:
        urllib.request.urlopen(q)
    except Exception:
        raise Exception('Failed to send message to elice.')


def _handle_image(filepath):
    mtype, _ = mimetypes.guess_type(filepath)

    if mtype is None or not mtype.startswith('image/'):
        raise ValueError('Invalid image filepath.')

    with open(filepath, 'rb') as f:
        data = 'data:%s;base64,%s' % (
            mtype,
            base64.b64encode(f.read()).decode('utf-8')
        )

    return data


def _handle_file(filepath):
    mtype, _ = mimetypes.guess_type(filepath)

    with open(filepath, 'rb') as f:
        data = '%s;data:%s;base64,%s' % (
            os.path.basename(filepath),
            mtype or 'application/octet-stream',
            base64.b64encode(f.read()).decode('utf-8')
        )

    return data


def send(msg_type, msg_data):
    _send(
        'http://%s:%s/comm/send/%s' % (EXECUTOR_IP,
                                       EXECUTOR_COM_PORT,
                                       EXECUTION_TOKEN),
        {'type': msg_type, 'data': msg_data}
    )


def send_image(filepath):
    send('image', _handle_image(filepath))


def send_file(filepath):
    send('file', _handle_file(filepath))


def secure_init():
    try:
        r = urllib.request.urlopen(
            'http://%s:%s/comm/secure/init/%s' % (EXECUTOR_IP,
                                                  EXECUTOR_COM_PORT,
                                                  EXECUTION_TOKEN)
        )
    except Exception:
        raise Exception('Failed to initialize elice util secure channel.')

    global _OTP_KEY
    _OTP_KEY = r.read().decode('utf-8')


def secure_send(msg_type, msg_data):
    _send(
        'http://%s:%s/comm/secure/send/%s/%s' % (EXECUTOR_IP,
                                                 EXECUTOR_COM_PORT,
                                                 EXECUTION_TOKEN,
                                                 _OTP_KEY),
        {'type': msg_type, 'data': msg_data}
    )


def secure_send_image(filepath):
    secure_send('image', _handle_image(filepath))


def secure_send_file(filepath):
    secure_send('file', _handle_file(filepath))


def secure_send_grader(msg):
    secure_send('grader', msg)


def secure_send_score(score):
    secure_send('score', score)