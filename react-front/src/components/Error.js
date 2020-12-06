import React, { useState } from 'react';
import Alert from 'react-bootstrap/Alert'


const Error = (props) => {
    const [show, setShow] = useState(true);
    if (show) {
        return (
            <Alert variant="danger" onClose={() => setShow(false)} dismissible>
                <Alert.Heading>Oh snap! You got an error!</Alert.Heading>
                <p>
                {props.errorMsg}
                </p>
            </Alert>
            // <div>Error: {props.errorMsg}</div>
        );
    } else {
        return (
            <div></div>
        );
    }
}

export default Error;