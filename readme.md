Create a new tag with id and get the randomly generated password:
```curl -d "tag_id=ASDFWWQERQWER123" -X POST http://127.0.0.1:8000/tag/new_tag/```

Create a new date for a given tag:
```curl -d "tag_id=ASDFWWQERQWER123&tag_pass=A63CF8756C368FB8&tag_datetime=09/19/19 12:26:16" -X POST http://127.0.0.1:8000/tag/new_date/```

Get validity of tag:
```curl -d "tag_id=ASDFWWQERQWER123&tag_pass=A63CF8756C368FB8" -X POST http://127.0.0.1:8000/tag/get_validity/```

Remove an existing tag:
```curl -d "tag_id=ASDFWWQERQWER123&tag_pass=A63CF8756C368FB8" -X POST http://127.0.0.1:8000/tag/rm_tag/```