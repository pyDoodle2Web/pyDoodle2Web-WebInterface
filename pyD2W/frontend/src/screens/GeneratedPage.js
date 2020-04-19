import React from 'react';

const GeneratedPage = (props) => {
    const html = props.html;
    return(
    <div dangerouslySetInnerHTML={{ __html: html }} />)
}

export default GeneratedPage;