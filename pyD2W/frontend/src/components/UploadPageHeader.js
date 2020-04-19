import React from 'react';

const UploadPageHeader = () => {
    return (
        <div>
        <img src="/static/img/pyDoodle2Web.png" alt="pyDoodle2Web-logo" className="img-fluid my-1"></img>
        <hr></hr>
        <h2>Upload your doodle</h2>
        <div className="alert alert-secondary pt-3">
            <p>Make sure your doodle has clear and visible lines and text. pyDoodle2Web currently works best with digitally
            drawn lines and text (MS paint drawn shapes).
        <br></br>
        To check out an example doodle,
        <a href="https://github.com/therexone/pyDoodle2Web/blob/master/referenceDoodle.png">click here. </a>
            </p>
        </div>
    </div>
    );
}

export default UploadPageHeader;