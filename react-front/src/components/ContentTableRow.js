
import React, { Component } from 'react';


class ContentTableRow extends Component {
    render() {
        return (
            <tr>
                <td>{this.props.txhash}</td>
                <td>{this.props.from}</td>
                <td>{this.props.to}</td>
                <td>{this.props.blockNo}</td>
                <td>{this.props.value * 1/1000000000000000000}</td>
                <td>{this.props.gasUsed}</td>
            </tr>
        )
    };
}

export default ContentTableRow;