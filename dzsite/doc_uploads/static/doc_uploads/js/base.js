Dropzone.autoDiscover = false;

const myDropzone = new Dropzone('#upload-dropzone', {
    url: 'upload/',
    maxFiles: 2,
    maxFilesize: 2,
    acceptedFiles: '.png, .jpg, .jpeg, .gif'
})