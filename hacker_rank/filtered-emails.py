def fun(s):
    # print(s)
    import re
    # return True if s is a valid email, else return False
    # It must have the username@websitename.extension format type.
    if len(s.split('@')) == 2 and int(len(s.split('@')[0])) > 0 and int(len(s.split('@')[1]) > 0):
        if len(s.split('@')[1].split('.')) == 2:
            # The username can only contain letters, digits, dashes and underscores.
            if '@' in s and s.count('@') <= 1 and '.' in s:
                # Check that email match `username@domain.extension`
                f1 = lambda x: True if re.findall(r'.*@\w+.\w{3}', x) is not None and len(
                    re.findall(r'.*@\w+.\w{3}', x)) > 0 else False
                f11 = lambda x: True if re.findall(r'.*@\w+.\w{2}', x) is not None and len(
                    re.findall(r'.*@\w+.\w{2}', x)) > 0 else False

                # The maximum length of the extension is 3.
                extension_lenght = len(s.split('.')[-1])
                f12 = lambda x: True if extension_lenght >= 2 and extension_lenght <= 3 else False

                # The website name can only have letters and digits.
                f2 = lambda x: True if len(re.findall(r'[^a-z0-9\-\.]', x.split('@')[1])) == 0 else False

                # extension only have letters
                f3 = lambda x: True if len(
                    re.findall(r'[0-9\<\>\/\\\{\}\[\]~:;.,()@_`]', x.split('@')[1].split('.')[-1])) == 0 else False

                # extension is present
                f4 = lambda x: True if re.findall(r'\.\w{3}', x) is not None and len(
                    re.findall(r'\.\w{3}', x)) > 0 else False
                f5 = lambda x: True if re.findall(r'\.\w{2}', x) is not None and len(
                    re.findall(r'\.\w{2}', x)) > 0 else False

                f6 = lambda x: True if len(re.findall(r'[^a-z0-9\-\_]', x.split('@')[0])) == 0 else False

                extension = f4(s) or f5(s)
                format_type = f1(s) or f11(s)

                status = True if format_type and f2(s) and f3(s) and extension and f12(s)and f6(s) is True else False

                print(s)
                print(format_type, extension, f2(s), f3(s), f12(s))
                print(status)
                print()
            else:
                status = False
            return status
        else:
            return False
    else:
        return False

def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    # n = int(input())
    # for _ in range(n):
    #     emails.append(input())

    emails = ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
    emails1 = ['dheeraj-234@gmail.com', 'itsallcrap', 'harsh_1234@rediff.in', 'kunal_shin@iop.az', 'matt23@@india.in']
    emails2 = ['iu89_in.plus@google.com', 'ill@google.com', 'fill@google1.com']
    emails3 = ['its@gmail.com1', 'mike13445@yahoomail9.server', 'rase23@ha_ch.com', 'daniyal@gmail.coma', 'thatisit@thatisit']
    emails4 = ['itsme@gmail', '@something', '@something.com', '@something.co1', 'sone.com']
    emails7 = ['learn.point@learningpoint.net', 'learnpoint@learningpoint.net', 'learnpoint@learningpoint.net1']
    filtered_emails = filter_mail(emails7)
    filtered_emails.sort()
    print(filtered_emails)
