import React, { useState, useEffect } from 'react';

const UploadForm = () => {
    const [formState, setFormState] = useState({
        carousel: false,
        navbar: false,
        upload: false
    });
    const [tags, setTags] = useState([])
    useEffect(() => {
        if (tags.length != 0) {
            setFormState((prevState) => ({ ...prevState, upload: true }))
        }
        if (tags.includes('navbar')) {
            setFormState((prevState) => ({ ...prevState, navbar: true }))
        }
        if (tags.includes('carousel')) {
            setFormState((prevState) => ({ ...prevState, carousel: true }))
        }
    }, [tags])

    return (
        <form
            className="form-group mt-4"
            id="form"
            onSubmit={async (e) => {
                e.preventDefault();
                const form = document.getElementById('form');
                const data = new FormData(form);
                let url ;
                if(!formState.upload){
                    url = '/readImage/';
                }else{
                    url = '/generate/'
                    data.append('tags', tags);
                }
                fetch(url, {
                    method: 'POST',
                    body: data,
                    headers: {
                        "X-CSRFToken": getCoockie('csrftoken')
                    }
                })
                    .then(resp => resp.json()
                    )
                    .then(data => {
                        if (!formState.upload) {
                            setTags(data.tags)
                        }
                        else{
                            console.log(data);
                        }
                    });
            }}
        >

            {
                !formState.upload &&
                <input className="" type="file" name="document" style={{ outline: "1px solid #afafaf", width: "50%" }} accept="image/*"></input>
            }

            {
                formState.navbar &&
                <div className="alert alert-success mt-4">
                    <p>A navbar was detected in the doodle. Enter a title for the Navbar: </p>
                    <input type="text" name="navbarTitle"></input>
                </div>
            }


            {
                formState.carousel &&
                <div className="alert alert-success mt-4 form-group d-inline-block">
                    <p>A carousel was detected in the doodle. Select the number of images in the carousel: </p>
                    <select name="carousel" className="form-control d-inline-block w-50" >
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                        <option value="6">6</option>
                        <option value="7">7</option>
                        <option value="8">8</option>
                        <option value="9">9</option>
                    </select>
                </div>
            }

            {
                formState.upload &&
                <button className="btn btn-dark ml-4 px-4" type="submit">Add customisation</button>
            }


            {
                !formState.upload &&
                <div className="d-inline-block mt-3 alert alert-primary w-50">
                    <input type="checkbox" name="darkMode" value='true' className="checkbox"></input>
                    <label className="ml-2 align-top d-inline" htmlFor="darkMode">Dark Mode (Adds dark theme to the generated html)</label>
                </div>
            }

            {
                !formState.upload &&
                <input className="btn btn-dark ml-4 px-4" type="submit"></input>
            }


        </form>
    );
}

const getCoockie = (name) => {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

export default UploadForm;