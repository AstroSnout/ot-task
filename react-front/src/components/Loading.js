import React from 'react';
import Spinner from 'react-bootstrap/Spinner';

const Loading = () => {
    return (
        <Spinner animation="border" role="status" id='loading-spinner'>
        </Spinner>
    );
}

export default Loading;