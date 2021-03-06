# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/16.
"""

from app.libs.success_code import Success
from app.libs.redprint import RedPrint
from app.models.banner import Banner
from app.validators.params import IDMustBePositiveInt

from app import doc

__author__ = 'Alimazing'

api = RedPrint('banner')


@api.route('/<int:id>', methods=['GET'])
@api.doc(doc.get_banner)
def get_banner(id):
	id = IDMustBePositiveInt().validate_for_api().id.data
	banner = Banner.get_banner_by_id(id=id)
	# banner.hide('description') # 临时隐藏
	return Success(banner)
