import React from 'react';
import UploadPageHeader from '../components/UploadPageHeader';
import UploadForm from '../components/UploadForm';

const UploadPage = (props) => {
    return (
        <div className="container px-lg-4 py-5">
            <UploadPageHeader />
            <UploadForm setHtml={props.setHtml} />
        </div>
    );
}

export default UploadPage;