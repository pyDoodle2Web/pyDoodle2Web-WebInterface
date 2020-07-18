import React from 'react';

interface Props {
    html: string
}


const GeneratedPage = (props: Props) => {
    const html = props.html;
    return(
    <div dangerouslySetInnerHTML={{ __html: html }} />)
}

export default GeneratedPage;