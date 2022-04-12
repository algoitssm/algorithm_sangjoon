import cx from 'classnames';
import { Component } from 'react';

export default class LikeButton extends Component {

    constructor(props){
        super(props);
        this.state = {
            active: false,
            likes: 100
        }
    }

    handleClick = () => {
        this.setState({
            active: !this.state.active,
            likes: this.state.active ? this.state.likes - 1 : this.state.likes + 1
        })
    }
    
    render() {
        const classes = cx({
            "like-button": true,
            "liked": this.state.active
            })
        return (
            <>
                <div>
                    <button className={classes} onClick={this.handleClick}>Like | <span className="likes-counter">{this.state.likes}</span></button>
                </div>
                <style>{`
                    .like-button {
                        font-size: 1rem;
                        padding: 5px 10px;
                        color:  #585858;
                    }
                   .liked {
                        font-weight: bold;
                        color: #1565c0;
                   }
                `}</style>
            </>
        );
    }
}
