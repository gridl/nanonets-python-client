# coding: utf-8

"""
    NanoNets

    Welcome to the NanoNets API! You can use our API to build custom deep learning models for images.<br/> We have language bindings in Shell, Ruby, Golang, Java, C# and Python! You can view code examples in the dark area to the right, and you can switch the programming language for the examples with the tabs in the top right. <br/> In the documentation, you will find ready to fire code samples in these languages as well as detailed API specs for different endpoints.<br/> # Model Object A model Object has 3 attributes<br/> ### model_id <b>Definition:</b> Unique Id for the model <br/><br/> ### model_type <b>Definition:</b> Type of model. Possible values are: <br/> <table>     <tr>         <td>classification</td>         <td>Image classification model</td>     </tr>     <tr>         <td>localization</td>         <td>Object detection model</td>     </tr>     <tr>         <td>multilabelclassification</td>         <td>Multi label image classification model</td>     </tr>     <tr>         <td>ocr</td>         <td>OCR model</td>     </tr> </table> <br/>  ### state <b>Definition:</b>Current state of model. Possible values are::<br/> <table>     <tr>         <td>-1</td>         <td>Error in model training</td>     </tr>     <tr>         <td>0</td>         <td>Model created. No training data uploaded yet</td>     </tr>     <tr>         <td>1</td>         <td>Training data uploaded. Need to annotate data</td>     </tr>     <tr>         <td>2</td>         <td>Training data annotated. Need to start training</td>     </tr>     <tr>         <td>3</td>         <td>Model in training queue</td>     </tr>     <tr>         <td>4</td>         <td>Model currently training</td>     </tr>     <tr>         <td>5</td>         <td>Model hosted. Can be used for prediction</td>     </tr> </table>   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@nanonets.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import nanonets
from models.upload_training_images_by_urlrequest import UploadTrainingImagesByUrlrequest  # noqa: E501
from nanonets.rest import ApiException


class TestUploadTrainingImagesByUrlrequest(unittest.TestCase):
    """UploadTrainingImagesByUrlrequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUploadTrainingImagesByUrlrequest(self):
        """Test UploadTrainingImagesByUrlrequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = nanonets.models.upload_training_images_by_urlrequest.UploadTrainingImagesByUrlrequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
