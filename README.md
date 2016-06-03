Custom Filters in Ansible
=========================

- Filter là 1 chức năng của jinja2 template. Trong ansible bạn cũng có thể thực hiện filter ngay trong playbooks. Phần lớn nhu cầu sẽ rơi vào các kiểu filter có sẵn. Có thể tham khảo các loại filter ở link cuối readme.md

Writing Your Own Filter
-----------------------

- Giả sử chúng ta cần cấu hình một dòng
```
ALLOWED_HOSTS = ["aekt.net", "opscloud.xyz", "cuonglm.xyz"]
```
Và có 1 danh sách tên miền trong biến domains
```
vars:
  domains:
    - aekt.net
    - opscloud.xyz
    - cuonglm.xyz
```
Jinja2 template:
```
ALLOWED_HOSTS = [{{ domains|join(", ") }}]
```
Kết quả khi gen templates sẽ là
```
ALLOWED_HOSTS = [aekt.net, opscloud.xyz, cuonglm.xyz]
```
Như vậy cần thêm một bộ filter để insert dấu “” vào để quote các string.
```
ALLOWED_HOSTS = [{{ domains|surround_by('"')|join(", ") }}]
```

- Không may là chức năng kiểu như bộ lọc `surround_by` không có sẵn. Nhưng Ansible cung cấp các API cho bạn tự dev 1 cái để dùng theo nhu cầu
.

```
def surround_by(a_list, c):
    if isinstance(a_list, list):
        return ['{c}{e}{c}'.format(c=c, e=e) for e in a_list]
    else:
        return a_list


class FilterModule(object):
    def filters(self):
        return {'surround_by': surround_by}
```

Trong đó:
- `surround_by` là tên function để sử dụng trong jinja2 filter.
- FilterModule class định nghĩa các filter method và trả về 1 từ điền với key là tên func, và value là function
- Bộ lọc được đặt đâu tùy thích, miễn sao có cấu hình trong ansible
```
filter_plugins = ./filter_plugins
```


- Ref link:
  +  http://stackoverflow.com/questions/15514365/add-quota-around-each-string-in-a-list-in-jinja2
  + http://docs.ansible.com/ansible/playbooks_filters.html
  + http://docs.ansible.com/ansible/developing_plugins.html#filter-plugins
  + https://github.com/ansible/ansible/tree/devel/lib/ansible/plugins/filter
