import React from 'react';
import axios from 'axios';
import CustomForm from '../components/Form'; 
import { Card } from  'antd';


class ArticleDetail extends React.Component {

    state = {
        article: {}
    }

    componentDidMount(){
        const articleID = this.props.match.params.articleID;
        axios.get(`http://localhost:8000/api/${articleID}`)
            .then(res => {
                this.setState({
                    article: res.data 
                });
            })
    } 
    
    render(){
        return(
            <div>
                <Card title={this.state.article.title}>
                    <p>{this.state.article.content}</p>
                </Card>
                <CustomForm/>
            </div>
        );
    }
}

export default ArticleDetail;