# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: pymammotion/proto/mctrl_nav.proto
# plugin: python-betterproto
from dataclasses import dataclass
from .common import *

import betterproto


@dataclass
class NavLatLonUp(betterproto.Message):
    lat: float = betterproto.double_field(1)
    lon: float = betterproto.double_field(2)


@dataclass
class NavBorderState(betterproto.Message):
    bdstate: int = betterproto.int32_field(1)


@dataclass
class NavPosUp(betterproto.Message):
    x: float = betterproto.float_field(1)
    y: float = betterproto.float_field(2)
    status: int = betterproto.int32_field(3)
    toward: int = betterproto.int32_field(4)
    stars: int = betterproto.int32_field(5)
    age: float = betterproto.float_field(6)
    lat_stddev: float = betterproto.float_field(7)
    lon_stddev: float = betterproto.float_field(8)
    l2df_stars: int = betterproto.int32_field(9)
    pos_type: int = betterproto.int32_field(10)
    c_hash_id: int = betterproto.int64_field(11)
    pos_level: int = betterproto.int32_field(12)


@dataclass
class NavBorderDataGetAck(betterproto.Message):
    job_id: int = betterproto.int32_field(1)
    current_frame: int = betterproto.int32_field(2)


@dataclass
class NavObstiBorderDataGet(betterproto.Message):
    obstacle_index: int = betterproto.int32_field(1)
    current_frame: int = betterproto.int32_field(2)
    obstacles_len: int = betterproto.int32_field(3)


@dataclass
class NavObstiBorderDataGetAck(betterproto.Message):
    obstacle_index: int = betterproto.int32_field(1)
    current_frame: int = betterproto.int32_field(2)


@dataclass
class NavCHlLineData(betterproto.Message):
    start_job_r_i: int = betterproto.int32_field(1)
    end_job_r_i: int = betterproto.int32_field(2)
    current_frame: int = betterproto.int32_field(3)
    channel_line_len: int = betterproto.int32_field(4)


@dataclass
class NavCHlLineDataAck(betterproto.Message):
    start_job_r_i: int = betterproto.int32_field(1)
    end_job_r_i: int = betterproto.int32_field(2)
    current_frame: int = betterproto.int32_field(3)


@dataclass
class NavTaskInfo(betterproto.Message):
    area: int = betterproto.int32_field(1)
    time: int = betterproto.int32_field(2)
    all_frame: int = betterproto.int32_field(3)
    current_frame: int = betterproto.int32_field(4)
    pathlen: int = betterproto.int32_field(5)
    dc: list["CommDataCouple"] = betterproto.message_field(6)


@dataclass
class NavBorderDataGet(betterproto.Message):
    job_id: int = betterproto.int32_field(1)
    current_frame: int = betterproto.int32_field(2)
    border_len: int = betterproto.int32_field(3)


@dataclass
class NavOptLineUp(betterproto.Message):
    start_job_r_i: int = betterproto.int32_field(1)
    end_job_r_i: int = betterproto.int32_field(2)
    all_frame: int = betterproto.int32_field(3)
    current_frame: int = betterproto.int32_field(4)
    channel_data_len: int = betterproto.int32_field(5)
    dc: list["CommDataCouple"] = betterproto.message_field(6)


@dataclass
class NavOptiBorderInfo(betterproto.Message):
    job_id: int = betterproto.int32_field(1)
    all_frame: int = betterproto.int32_field(2)
    current_frame: int = betterproto.int32_field(3)
    border_data_len: int = betterproto.int32_field(4)
    dc: list["CommDataCouple"] = betterproto.message_field(5)


@dataclass
class NavOptObsInfo(betterproto.Message):
    obstacle_id: int = betterproto.int32_field(1)
    all_frame: int = betterproto.int32_field(2)
    current_frame: int = betterproto.int32_field(3)
    obstacle_data_len: int = betterproto.int32_field(4)
    dc: list["CommDataCouple"] = betterproto.message_field(5)


@dataclass
class NavStartJob(betterproto.Message):
    job_id: int = betterproto.int64_field(1)
    job_ver: int = betterproto.int32_field(2)
    job_mode: int = betterproto.int32_field(3)
    rain_tactics: int = betterproto.int32_field(4)
    knife_height: int = betterproto.int32_field(5)
    speed: float = betterproto.float_field(6)
    channel_width: int = betterproto.int32_field(7)
    ultra_wave: int = betterproto.int32_field(8)
    channel_mode: int = betterproto.int32_field(9)


@dataclass
class NavTaskProgress(betterproto.Message):
    task_progress: int = betterproto.int32_field(1)


@dataclass
class NavResFrame(betterproto.Message):
    frameid: int = betterproto.int32_field(1)


@dataclass
class NavGetHashList(betterproto.Message):
    pver: int = betterproto.int32_field(1)
    sub_cmd: int = betterproto.int32_field(2)
    total_frame: int = betterproto.int32_field(3)
    current_frame: int = betterproto.int32_field(4)
    data_hash: float = betterproto.fixed64_field(5)
    reserved: str = betterproto.string_field(6)


@dataclass
class NavGetHashListAck(betterproto.Message):
    pver: int = betterproto.int32_field(1)
    sub_cmd: int = betterproto.int32_field(2)
    total_frame: int = betterproto.int32_field(3)
    current_frame: int = betterproto.int32_field(4)
    data_hash: float = betterproto.fixed64_field(5)
    hash_len: int = betterproto.int32_field(6)
    reserved: str = betterproto.string_field(7)
    result: int = betterproto.int32_field(8)
    data_couple: list[int] = betterproto.int64_field(13)


@dataclass
class NavGetCommData(betterproto.Message):
    pver: int = betterproto.int32_field(1)
    sub_cmd: int = betterproto.int32_field(2)
    action: int = betterproto.int32_field(3)
    type: int = betterproto.int32_field(4)
    hash: int = betterproto.int64_field(5)
    paternal_hash_a: int = betterproto.int64_field(6)
    paternal_hash_b: int = betterproto.int64_field(7)
    total_frame: int = betterproto.int32_field(8)
    current_frame: int = betterproto.int32_field(9)
    data_hash: float = betterproto.fixed64_field(10)
    reserved: str = betterproto.string_field(11)


@dataclass
class NavGetCommDataAck(betterproto.Message):
    pver: int = betterproto.int32_field(1)
    sub_cmd: int = betterproto.int32_field(2)
    result: int = betterproto.int32_field(3)
    action: int = betterproto.int32_field(4)
    type: int = betterproto.int32_field(5)
    hash: float = betterproto.fixed64_field(6)
    paternal_hash_a: float = betterproto.fixed64_field(7)
    paternal_hash_b: float = betterproto.fixed64_field(8)
    total_frame: int = betterproto.int32_field(9)
    current_frame: int = betterproto.int32_field(10)
    data_hash: float = betterproto.fixed64_field(11)
    data_len: int = betterproto.int32_field(12)
    data_couple: list["CommDataCouple"] = betterproto.message_field(13)
    reserved: str = betterproto.string_field(14)


@dataclass
class NavReqCoverPath(betterproto.Message):
    pver: int = betterproto.int32_field(1)
    job_id: int = betterproto.int64_field(2)
    job_ver: int = betterproto.int32_field(3)
    job_mode: int = betterproto.int32_field(4)
    sub_cmd: int = betterproto.int32_field(5)
    edge_mode: int = betterproto.int32_field(6)
    knife_height: int = betterproto.int32_field(7)
    channel_width: int = betterproto.int32_field(8)
    ultra_wave: int = betterproto.int32_field(9)
    channel_mode: int = betterproto.int32_field(10)
    toward: int = betterproto.int32_field(11)
    speed: float = betterproto.float_field(12)
    zone_hashs: list[float] = betterproto.fixed64_field(13)
    path_hash: float = betterproto.fixed64_field(14)
    reserved: str = betterproto.string_field(15)
    result: int = betterproto.int32_field(16)
    toward_mode: int = betterproto.int32_field(17)
    toward_included_angle: int = betterproto.int32_field(18)


@dataclass
class NavUploadZigZagResult(betterproto.Message):
    pver: int = betterproto.int32_field(1)
    job_id: int = betterproto.int64_field(2)
    job_ver: int = betterproto.int32_field(3)
    result: int = betterproto.int32_field(4)
    area: int = betterproto.int32_field(5)
    time: int = betterproto.int32_field(6)
    total_zone_num: int = betterproto.int32_field(7)
    current_zone_path_num: int = betterproto.int32_field(8)
    current_zone_path_id: int = betterproto.int32_field(9)
    current_zone: int = betterproto.int32_field(10)
    current_hash: float = betterproto.fixed64_field(11)
    total_frame: int = betterproto.int32_field(12)
    current_frame: int = betterproto.int32_field(13)
    channel_mode: int = betterproto.int32_field(14)
    channel_mode_id: int = betterproto.int32_field(15)
    data_hash: float = betterproto.fixed64_field(16)
    data_len: int = betterproto.int32_field(17)
    reserved: str = betterproto.string_field(18)
    data_couple: list["CommDataCouple"] = betterproto.message_field(19)
    sub_cmd: int = betterproto.int32_field(20)


@dataclass
class NavUploadZigZagResultAck(betterproto.Message):
    pver: int = betterproto.int32_field(1)
    current_zone: int = betterproto.int32_field(2)
    current_hash: float = betterproto.fixed64_field(3)
    total_frame: int = betterproto.int32_field(4)
    current_frame: int = betterproto.int32_field(5)
    data_hash: float = betterproto.fixed64_field(6)
    reserved: str = betterproto.string_field(7)
    sub_cmd: int = betterproto.int32_field(8)


@dataclass
class NavTaskCtrl(betterproto.Message):
    type: int = betterproto.int32_field(1)
    action: int = betterproto.int32_field(2)
    result: int = betterproto.int32_field(3)
    reserved: str = betterproto.string_field(4)


@dataclass
class NavTaskIdRw(betterproto.Message):
    pver: int = betterproto.int32_field(1)
    sub_cmd: int = betterproto.int32_field(2)
    task_name: str = betterproto.string_field(3)
    task_id: str = betterproto.string_field(4)
    result: int = betterproto.int32_field(5)
    reserved: str = betterproto.string_field(6)


@dataclass
class NavSysHashOverview(betterproto.Message):
    commonhash_overview: float = betterproto.fixed64_field(1)
    path_hash_overview: float = betterproto.fixed64_field(2)


@dataclass
class NavTaskBreakPoint(betterproto.Message):
    x: float = betterproto.float_field(1)
    y: float = betterproto.float_field(2)
    toward: int = betterproto.int32_field(3)
    flag: int = betterproto.int32_field(4)
    action: int = betterproto.int32_field(5)
    zone_hash: float = betterproto.fixed64_field(6)


@dataclass
class NavPlanJobSet(betterproto.Message):
    pver: int = betterproto.int32_field(1)
    sub_cmd: int = betterproto.int32_field(2)
    area: int = betterproto.int32_field(3)
    work_time: int = betterproto.int32_field(4)
    version: str = betterproto.string_field(5)
    id: str = betterproto.string_field(6)
    user_id: str = betterproto.string_field(7)
    device_id: str = betterproto.string_field(8)
    plan_id: str = betterproto.string_field(9)
    task_id: str = betterproto.string_field(10)
    job_id: str = betterproto.string_field(11)
    start_time: str = betterproto.string_field(12)
    end_time: str = betterproto.string_field(13)
    week: int = betterproto.int32_field(14)
    knife_height: int = betterproto.int32_field(15)
    model: int = betterproto.int32_field(16)
    edge_mode: int = betterproto.int32_field(17)
    required_time: int = betterproto.int32_field(18)
    route_angle: int = betterproto.int32_field(19)
    route_model: int = betterproto.int32_field(20)
    route_spacing: int = betterproto.int32_field(21)
    ultrasonic_barrier: int = betterproto.int32_field(22)
    total_plan_num: int = betterproto.int32_field(23)
    plan_index: int = betterproto.int32_field(24)
    result: int = betterproto.int32_field(25)
    speed: float = betterproto.float_field(26)
    task_name: str = betterproto.string_field(27)
    job_name: str = betterproto.string_field(28)
    zone_hashs: list[float] = betterproto.fixed64_field(29)
    reserved: str = betterproto.string_field(30)
    start_date: str = betterproto.string_field(31)
    end_date: str = betterproto.string_field(32)
    trigger_type: int = betterproto.int32_field(33)
    day: int = betterproto.int32_field(34)
    weeks: list[float] = betterproto.fixed32_field(35)
    remained_seconds: int = betterproto.int64_field(36)
    toward_mode: int = betterproto.int32_field(37)
    toward_included_angle: int = betterproto.int32_field(38)


@dataclass
class NavUnableTimeSet(betterproto.Message):
    sub_cmd: int = betterproto.int32_field(1)
    device_id: str = betterproto.string_field(2)
    unable_start_time: str = betterproto.string_field(3)
    unable_end_time: str = betterproto.string_field(4)
    result: int = betterproto.int32_field(5)
    reserved: str = betterproto.string_field(6)


@dataclass
class ChargePileType(betterproto.Message):
    toward: int = betterproto.int32_field(1)
    x: float = betterproto.float_field(2)
    y: float = betterproto.float_field(3)


@dataclass
class SimulationCmdData(betterproto.Message):
    sub_cmd: int = betterproto.int32_field(1)
    param_id: int = betterproto.int32_field(2)
    param_value: list[int] = betterproto.int32_field(3)


@dataclass
class WorkReportUpdateCmd(betterproto.Message):
    sub_cmd: int = betterproto.int32_field(1)


@dataclass
class WorkReportUpdateAck(betterproto.Message):
    update_flag: bool = betterproto.bool_field(1)
    info_num: int = betterproto.int32_field(2)


@dataclass
class WorkReportCmdData(betterproto.Message):
    sub_cmd: int = betterproto.int32_field(1)
    get_info_num: int = betterproto.int32_field(2)


@dataclass
class WorkReportInfoAck(betterproto.Message):
    interrupt_flag: bool = betterproto.bool_field(1)
    start_work_time: int = betterproto.int64_field(2)
    end_work_time: int = betterproto.int64_field(3)
    work_time_used: int = betterproto.int32_field(4)
    work_ares: float = betterproto.double_field(5)
    work_progress: int = betterproto.int32_field(6)
    height_of_knife: int = betterproto.int32_field(7)
    work_type: int = betterproto.int32_field(8)
    work_result: int = betterproto.int32_field(9)
    total_ack_num: int = betterproto.int32_field(10)
    current_ack_num: int = betterproto.int32_field(11)


@dataclass
class AppRequestCoverPathsT(betterproto.Message):
    pver: int = betterproto.int32_field(1)
    sub_cmd: int = betterproto.int32_field(2)
    total_frame: int = betterproto.int32_field(3)
    current_frame: int = betterproto.int32_field(4)
    data_hash: float = betterproto.fixed64_field(5)
    transaction_id: int = betterproto.int64_field(6)
    reserved: list[int] = betterproto.int64_field(7)
    hash_list: list[float] = betterproto.fixed64_field(8)


@dataclass
class CoverPathPacketT(betterproto.Message):
    path_hash: float = betterproto.fixed64_field(1)
    path_type: int = betterproto.int32_field(2)
    path_total: int = betterproto.int32_field(3)
    path_cur: int = betterproto.int32_field(4)
    zone_hash: float = betterproto.fixed64_field(5)
    data_couple: list["CommDataCouple"] = betterproto.message_field(6)


@dataclass
class CoverPathUploadT(betterproto.Message):
    pver: int = betterproto.int32_field(1)
    result: int = betterproto.int32_field(2)
    sub_cmd: int = betterproto.int32_field(3)
    area: int = betterproto.int32_field(4)
    time: int = betterproto.int32_field(5)
    total_frame: int = betterproto.int32_field(6)
    current_frame: int = betterproto.int32_field(7)
    total_path_num: int = betterproto.int32_field(8)
    vaild_path_num: int = betterproto.int32_field(9)
    data_hash: float = betterproto.fixed64_field(10)
    transaction_id: int = betterproto.int64_field(11)
    reserved: list[int] = betterproto.int64_field(12)
    data_len: int = betterproto.int32_field(13)
    path_packets: list["CoverPathPacketT"] = betterproto.message_field(14)


@dataclass
class ZoneStartPrecentT(betterproto.Message):
    data_hash: float = betterproto.fixed64_field(1)
    x: float = betterproto.float_field(2)
    y: float = betterproto.float_field(3)
    index: int = betterproto.int32_field(4)


@dataclass
class VisionCtrlMsg(betterproto.Message):
    type: int = betterproto.int32_field(1)
    cmd: int = betterproto.int32_field(2)


@dataclass
class NavSysParamMsg(betterproto.Message):
    rw: int = betterproto.int32_field(1)
    id: int = betterproto.int32_field(2)
    context: int = betterproto.int32_field(3)


@dataclass
class NavPlanTaskExecute(betterproto.Message):
    sub_cmd: int = betterproto.int32_field(1)
    id: str = betterproto.string_field(2)
    name: str = betterproto.string_field(3)
    result: int = betterproto.int32_field(4)


@dataclass
class CostmapT(betterproto.Message):
    width: int = betterproto.int32_field(1)
    height: int = betterproto.int32_field(2)
    center_x: float = betterproto.float_field(3)
    center_y: float = betterproto.float_field(4)
    yaw: float = betterproto.float_field(5)
    res: float = betterproto.float_field(6)
    costmap: list[int] = betterproto.int32_field(7)


@dataclass
class PlanTaskNameIdT(betterproto.Message):
    id: str = betterproto.string_field(1)
    name: str = betterproto.string_field(2)


@dataclass
class NavGetAllPlanTask(betterproto.Message):
    tasks: list["PlanTaskNameIdT"] = betterproto.message_field(1)


@dataclass
class NavTaskCtrlAck(betterproto.Message):
    """Define the NavTaskCtrlAck message"""

    type: int = betterproto.int32_field(1)
    action: int = betterproto.int32_field(2)
    result: int = betterproto.int32_field(3)
    nav_state: int = betterproto.int32_field(4)
    reserved: str = betterproto.string_field(5)


@dataclass
class NavMapNameMsg(betterproto.Message):
    rw: int = betterproto.int32_field(1)
    hash: int = betterproto.int64_field(2)
    name: str = betterproto.string_field(3)
    result: int = betterproto.int32_field(4)
    device_id: str = betterproto.string_field(5)


@dataclass
class SvgMessageT(betterproto.Message):
    x_move: float = betterproto.double_field(1)
    y_move: float = betterproto.double_field(2)
    scale: float = betterproto.double_field(3)
    rotate: float = betterproto.double_field(4)
    base_width_m: float = betterproto.double_field(5)
    base_width_pix: int = betterproto.int32_field(7)
    base_height_m: float = betterproto.double_field(6)
    base_height_pix: int = betterproto.int32_field(8)
    data_count: int = betterproto.int32_field(12)
    hide_svg: bool = betterproto.bool_field(13)
    name_count: int = betterproto.int32_field(11)
    svg_file_name: str = betterproto.string_field(9)
    svg_file_data: str = betterproto.string_field(10)


@dataclass
class SvgMessageAckT(betterproto.Message):
    pver: int = betterproto.int32_field(1)
    sub_cmd: int = betterproto.int32_field(2)
    total_frame: int = betterproto.int32_field(3)
    current_frame: int = betterproto.int32_field(4)
    data_hash: int = betterproto.int64_field(5)
    paternal_hash_a: int = betterproto.int64_field(6)
    type: int = betterproto.int32_field(7)
    result: int = betterproto.int32_field(8)
    svg_message: "SvgMessageT" = betterproto.message_field(9)


@dataclass
class AreaHashName(betterproto.Message):
    # Define fields for AreaHashName message here For example:
    name: str = betterproto.string_field(1)
    hash: int = betterproto.int64_field(2)


@dataclass
class AppGetAllAreaHashName(betterproto.Message):
    device_id: str = betterproto.string_field(1)
    hashnames: list["AreaHashName"] = betterproto.message_field(2)


@dataclass
class MctlNav(betterproto.Message):
    toapp_lat_up: "NavLatLonUp" = betterproto.message_field(1, group="SubNavMsg")
    toapp_pos_up: "NavPosUp" = betterproto.message_field(2, group="SubNavMsg")
    todev_chl_line_data: "NavCHlLineData" = betterproto.message_field(
        3, group="SubNavMsg"
    )
    toapp_task_info: "NavTaskInfo" = betterproto.message_field(4, group="SubNavMsg")
    toapp_opt_line_up: "NavOptLineUp" = betterproto.message_field(5, group="SubNavMsg")
    toapp_opt_border_info: "NavOptiBorderInfo" = betterproto.message_field(
        6, group="SubNavMsg"
    )
    toapp_opt_obs_info: "NavOptObsInfo" = betterproto.message_field(
        7, group="SubNavMsg"
    )
    todev_task_info_ack: "NavResFrame" = betterproto.message_field(8, group="SubNavMsg")
    todev_opt_border_info_ack: "NavResFrame" = betterproto.message_field(
        9, group="SubNavMsg"
    )
    todev_opt_obs_info_ack: "NavResFrame" = betterproto.message_field(
        10, group="SubNavMsg"
    )
    todev_opt_line_up_ack: "NavResFrame" = betterproto.message_field(
        11, group="SubNavMsg"
    )
    toapp_chgpileto: "ChargePileType" = betterproto.message_field(12, group="SubNavMsg")
    todev_sustask: int = betterproto.int32_field(13, group="SubNavMsg")
    todev_rechgcmd: int = betterproto.int32_field(14, group="SubNavMsg")
    todev_edgecmd: int = betterproto.int32_field(15, group="SubNavMsg")
    todev_draw_border: int = betterproto.int32_field(16, group="SubNavMsg")
    todev_draw_border_end: int = betterproto.int32_field(17, group="SubNavMsg")
    todev_draw_obs: int = betterproto.int32_field(18, group="SubNavMsg")
    todev_draw_obs_end: int = betterproto.int32_field(19, group="SubNavMsg")
    todev_chl_line: int = betterproto.int32_field(20, group="SubNavMsg")
    todev_chl_line_end: int = betterproto.int32_field(21, group="SubNavMsg")
    todev_save_task: int = betterproto.int32_field(22, group="SubNavMsg")
    todev_cancel_suscmd: int = betterproto.int32_field(23, group="SubNavMsg")
    todev_reset_chg_pile: int = betterproto.int32_field(24, group="SubNavMsg")
    todev_cancel_draw_cmd: int = betterproto.int32_field(25, group="SubNavMsg")
    todev_one_touch_leave_pile: int = betterproto.int32_field(26, group="SubNavMsg")
    todev_mow_task: "NavStartJob" = betterproto.message_field(27, group="SubNavMsg")
    toapp_bstate: "NavBorderState" = betterproto.message_field(28, group="SubNavMsg")
    todev_lat_up_ack: int = betterproto.int32_field(29, group="SubNavMsg")
    todev_gethash: "NavGetHashList" = betterproto.message_field(30, group="SubNavMsg")
    toapp_gethash_ack: "NavGetHashListAck" = betterproto.message_field(
        31, group="SubNavMsg"
    )
    todev_get_commondata: "NavGetCommData" = betterproto.message_field(
        32, group="SubNavMsg"
    )
    toapp_get_commondata_ack: "NavGetCommDataAck" = betterproto.message_field(
        33, group="SubNavMsg"
    )
    bidire_reqconver_path: "NavReqCoverPath" = betterproto.message_field(
        34, group="SubNavMsg"
    )
    toapp_zigzag: "NavUploadZigZagResult" = betterproto.message_field(
        35, group="SubNavMsg"
    )
    todev_zigzag_ack: "NavUploadZigZagResultAck" = betterproto.message_field(
        36, group="SubNavMsg"
    )
    todev_taskctrl: "NavTaskCtrl" = betterproto.message_field(37, group="SubNavMsg")
    bidire_taskid: "NavTaskIdRw" = betterproto.message_field(38, group="SubNavMsg")
    toapp_bp: "NavTaskBreakPoint" = betterproto.message_field(39, group="SubNavMsg")
    todev_planjob_set: "NavPlanJobSet" = betterproto.message_field(
        40, group="SubNavMsg"
    )
    todev_unable_time_set: "NavUnableTimeSet" = betterproto.message_field(
        41, group="SubNavMsg"
    )
    simulation_cmd: "SimulationCmdData" = betterproto.message_field(
        42, group="SubNavMsg"
    )
    todev_work_report_update_cmd: "WorkReportUpdateCmd" = betterproto.message_field(
        43, group="SubNavMsg"
    )
    toapp_work_report_update_ack: "WorkReportUpdateAck" = betterproto.message_field(
        44, group="SubNavMsg"
    )
    todev_work_report_cmd: "WorkReportCmdData" = betterproto.message_field(
        45, group="SubNavMsg"
    )
    toapp_work_report_ack: "WorkReportInfoAck" = betterproto.message_field(
        46, group="SubNavMsg"
    )
    toapp_work_report_upload: "WorkReportInfoAck" = betterproto.message_field(
        47, group="SubNavMsg"
    )
    app_request_cover_paths: "AppRequestCoverPathsT" = betterproto.message_field(
        48, group="SubNavMsg"
    )
    cover_path_upload: "CoverPathUploadT" = betterproto.message_field(
        49, group="SubNavMsg"
    )
    zone_start_precent: "ZoneStartPrecentT" = betterproto.message_field(
        50, group="SubNavMsg"
    )
    vision_ctrl: "VisionCtrlMsg" = betterproto.message_field(51, group="SubNavMsg")
    nav_sys_param_cmd: "NavSysParamMsg" = betterproto.message_field(
        52, group="SubNavMsg"
    )
    plan_task_execute: "NavPlanTaskExecute" = betterproto.message_field(
        53, group="SubNavMsg"
    )
    toapp_costmap: "CostmapT" = betterproto.message_field(54, group="SubNavMsg")
    plan_task_name_id: "PlanTaskNameIdT" = betterproto.message_field(
        55, group="SubNavMsg"
    )
    all_plan_task: "NavGetAllPlanTask" = betterproto.message_field(
        56, group="SubNavMsg"
    )
    todev_taskctrl_ack: "NavTaskCtrlAck" = betterproto.message_field(
        57, group="SubNavMsg"
    )
    toapp_map_name_msg: "NavMapNameMsg" = betterproto.message_field(
        58, group="SubNavMsg"
    )
    todev_svg_msg: "SvgMessageAckT" = betterproto.message_field(59, group="SubNavMsg")
    toapp_svg_msg: "SvgMessageAckT" = betterproto.message_field(60, group="SubNavMsg")
    toapp_all_hash_name: "AppGetAllAreaHashName" = betterproto.message_field(
        61, group="SubNavMsg"
    )
