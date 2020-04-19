import React from 'react';
import UploadPageHeader from '../components/UploadPageHeader';
import UploadForm from '../components/UploadForm';

const UploadPage = () => {
    return (
        <div className="container px-lg-4 py-5">
            <UploadPageHeader />
            <UploadForm />
        </div>
    );
}

export default UploadPage;