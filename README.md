# Django Employee App

I spent some time this weekend implementing a basic Django app from the scratch. It's possible to test the results by either downloading and running this repository locally or by acessing: [web app hosted on heroku](https://dpiassi-django.herokuapp.com/)

## Deliverables

- A Django admin panel to manage employees` data.
- A Django API to list (`GET`), add (`POST`) and remove (`DELETE`) employees.

## Paths

- [/admin/](https://dpiassi-django.herokuapp.com/admin/): Django admin panel to manage employees, users and groups.
- [/employee/](https://dpiassi-django.herokuapp.com/employee/): page showcasing the `/employee/` endpoint of Django REST API.
- [/employee/$id/](https://dpiassi-django.herokuapp.com/employee/1/): this API panel allows any user to `GET` and `DELETE` specified employee
- [/home/](https://dpiassi-django.herokuapp.com/home/): very basic Front-End, adapted from VS Code tutorial

## API Example (list)

### Request

```bash
curl -H "Content-Type: application/javascript" https://dpiassi-django.herokuapp.com/employee/
```

### Response

```js
[
  {
    id: 4,
    name: "Mauricio Alegretti",
    email: "mauricio.alegretti@igs-software.com.br",
    created_at: "2022-06-26T19:55:42.091774Z",
    updated_at: "2022-06-26T19:55:42.091799Z",
    department: "HR",
  },
  {
    id: 3,
    name: "Tatiane Laura",
    email: "tatiane.laura@igs-software.com.br",
    created_at: "2022-06-26T19:55:15.883715Z",
    updated_at: "2022-06-26T19:55:15.883733Z",
    department: "DEV",
  },
  {
    id: 2,
    name: "Felipe Morais",
    email: "felipe.morais@igs-software.com.br",
    created_at: "2022-06-26T19:54:48.448678Z",
    updated_at: "2022-06-26T19:54:48.448699Z",
    department: "TES",
  },
];
```
