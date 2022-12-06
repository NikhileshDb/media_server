const currentOpenedUrl = window.location.pathname
const progressEl = document.querySelector('.progress__indicator');
const csrf_token = Cookies.get('csrftoken');




if (currentOpenedUrl == "/upload-new/") {

    const videoInputEl = document.querySelector('#video_input');
    const submitButtonEl = document.querySelector('#submit_button');
    submitButtonEl.addEventListener('click', async (e) => {
        e.preventDefault();
        axios.post('http://127.0.0.1:8000/api/upload-new/', {
            "video_file": videoInputEl.files[0],
            "name": "",
        }, {
            headers: {
                'Content-Type': 'multipart/form-data',
                'X-CSRFToken': csrf_token,

            },
            onUploadProgress: function (progressEvent) {
                var percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total)
                progressEl.setAttribute('aria-valuenow', percentCompleted);
                progressEl.style.width = `${percentCompleted}%`;
                progressEl.innerHTML = `${percentCompleted}%`;
            }

        }).then(function (res) {
            var new_div = document.createElement('div');
            new_div.appendChild(document.createTextNode('UploadProgress Completed.'));
            const progressWrapper = document.querySelector('.progress');
            document.body.insertBefore(new_div, progressWrapper);
            videoInputEl.value = '';
            console.log(res);
        }).catch((error) => {
            console.log(error);
        })

    });
}

const createPackageButton = document.querySelector('#create_package_btn');
createPackageButton.addEventListener('click', function (e) {
    e.preventDefault();
    axios.post('http://127.0.0.1:8000/api/start-packaging/', {
        "object_id": createPackageButton.value,
    }, {
        headers: {
            'X-CSRFToken': csrf_token,
        }
    }).then((res) => {
        task_id = res['data'].task_id
        let ws = new WebSocket(`ws://127.0.0.1:8000/ws/packaging-task/${task_id}/`);
        ws.onopen = (e) => {
            ws.send("Helo, initiate the task for packaging.")
        }
        ws.onmessage = (event) => {
            console.log(event['data']);
        }

    }).catch((err) => {
        console.log(err);
    });
})