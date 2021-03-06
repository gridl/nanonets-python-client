# coding: utf-8

"""
    NanoNets

    Welcome to the NanoNets API! You can use our API to build custom deep learning models for images.<br/> We have language bindings in Shell, Ruby, Golang, Java, C# and Python! You can view code examples in the dark area to the right, and you can switch the programming language for the examples with the tabs in the top right. <br/> In the documentation, you will find ready to fire code samples in these languages as well as detailed API specs for different endpoints.<br/> # Model Object A model Object has 3 attributes<br/> ### model_id <b>Definition:</b> Unique Id for the model <br/><br/> ### model_type <b>Definition:</b> Type of model. Possible values are: <br/> <table>     <tr>         <td>classification</td>         <td>Image classification model</td>     </tr>     <tr>         <td>localization</td>         <td>Object detection model</td>     </tr>     <tr>         <td>multilabelclassification</td>         <td>Multi label image classification model</td>     </tr>     <tr>         <td>ocr</td>         <td>OCR model</td>     </tr> </table> <br/>  ### state <b>Definition:</b>Current state of model. Possible values are::<br/> <table>     <tr>         <td>-1</td>         <td>Error in model training</td>     </tr>     <tr>         <td>0</td>         <td>Model created. No training data uploaded yet</td>     </tr>     <tr>         <td>1</td>         <td>Training data uploaded. Need to annotate data</td>     </tr>     <tr>         <td>2</td>         <td>Training data annotated. Need to start training</td>     </tr>     <tr>         <td>3</td>         <td>Model in training queue</td>     </tr>     <tr>         <td>4</td>         <td>Model currently training</td>     </tr>     <tr>         <td>5</td>         <td>Model hosted. Can be used for prediction</td>     </tr> </table>   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@nanonets.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from nanonets.api_client import ApiClient


class MultiLabelClassificationModelApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def multi_label_classification_by_model_id_get(self, model_id, **kwargs):  # noqa: E501
        """Get Model by Id  # noqa: E501

        This endpoint retrieves a specific model's details given it's id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.multi_label_classification_by_model_id_get(model_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str model_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.multi_label_classification_by_model_id_get_with_http_info(model_id, **kwargs)  # noqa: E501
        else:
            (data) = self.multi_label_classification_by_model_id_get_with_http_info(model_id, **kwargs)  # noqa: E501
            return data

    def multi_label_classification_by_model_id_get_with_http_info(self, model_id, **kwargs):  # noqa: E501
        """Get Model by Id  # noqa: E501

        This endpoint retrieves a specific model's details given it's id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.multi_label_classification_by_model_id_get_with_http_info(model_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str model_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['model_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method multi_label_classification_by_model_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'model_id' is set
        if ('model_id' not in params or
                params['model_id'] is None):
            raise ValueError("Missing the required parameter `model_id` when calling `multi_label_classification_by_model_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'model_id' in params:
            path_params['model_id'] = params['model_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/MultiLabelClassification/Model/{model_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def multi_label_image_classification_post(self, body, content_type, **kwargs):  # noqa: E501
        """Create New Model  # noqa: E501

        You can create a new model using this endpoint. A successful API call will return the json structure of the newly created model. You can then use the model's id to upload images for each category and then retrain the model.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.multi_label_image_classification_post(body, content_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateNewModelrequest body: (required)
        :param str content_type: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.multi_label_image_classification_post_with_http_info(body, content_type, **kwargs)  # noqa: E501
        else:
            (data) = self.multi_label_image_classification_post_with_http_info(body, content_type, **kwargs)  # noqa: E501
            return data

    def multi_label_image_classification_post_with_http_info(self, body, content_type, **kwargs):  # noqa: E501
        """Create New Model  # noqa: E501

        You can create a new model using this endpoint. A successful API call will return the json structure of the newly created model. You can then use the model's id to upload images for each category and then retrain the model.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.multi_label_image_classification_post_with_http_info(body, content_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateNewModelrequest body: (required)
        :param str content_type: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'content_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method multi_label_image_classification_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `multi_label_image_classification_post`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `multi_label_image_classification_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/MultiLabelClassification/Model/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
